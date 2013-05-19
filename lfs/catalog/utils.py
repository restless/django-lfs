# python imports
import math

# django imports
from django.conf import settings
from django.core.cache import cache
from django.db import connection
from django.core.exceptions import FieldError

# import lfs
from django.utils import translation
import lfs.catalog.models
from lfs.catalog.settings import CONFIGURABLE_PRODUCT
from lfs.catalog.settings import STANDARD_PRODUCT
from lfs.catalog.settings import PRODUCT_WITH_VARIANTS
from lfs.catalog.settings import PROPERTY_VALUE_TYPE_FILTER

# Load logger
import logging
from lfs.core.translation_utils import build_localized_fieldname, get_languages_list

logger = logging.getLogger("default")


# TODO: Add unit test
def get_current_top_category(request, obj):
    """
    Returns the current top category of a product.
    """
    if obj.__class__.__name__.lower() == "product":
        category = obj.get_current_category(request)
    else:
        category = obj

    if category is None:
        return category

    while category.parent is not None:
        category = category.parent

    return category


def get_price_filters(category, product_filter, price_filter):
    """Creates price filter links based on the min and max price of the
    categorie's products.
    """
    # Base are the filtered products
    products = get_filtered_products_for_category(category, product_filter, price_filter, None)
    if not products:
        return []

    # And their variants
    all_products = []
    for product in products:
        all_products.extend(product.variants.filter(active=True))
        if product.is_product_with_variants():
            all_products.extend(product.variants.filter(active=True))
        else:
            all_products.append(product)

    product_ids = [p.id for p in all_products]

    # If a price filter is set we return just this.
    if price_filter:
        min = price_filter["min"]
        max = price_filter["max"]
        products = lfs.catalog.models.Product.objects.filter(
            effective_price__range=(min, max), pk__in=product_ids)

        return {
            "show_reset": True,
            "show_quantity": False,
            "items": [{"min": float(min), "max": float(max)}],
            }

    product_ids_str = ", ".join([str(p.id) for p in all_products])
    cursor = connection.cursor()
    cursor.execute("""SELECT min(effective_price), max(effective_price)
                      FROM catalog_product
                      WHERE id IN (%s)""" % product_ids_str)

    pmin, pmax = cursor.fetchall()[0]
    if pmax == pmin:
        step = pmax
    else:
        diff = pmax - pmin
        step = diff / 3

    if step >= 0 and step < 3:
        step = 3
    elif step >= 3 and step < 6:
        step = 5
    elif step >= 6 and step < 11:
        step = 10
    elif step >= 11 and step < 51:
        step = 50
    elif step >= 51 and step < 101:
        step = 100
    elif step >= 101 and step < 501:
        step = 500
    elif step >= 501 and step < 1001:
        step = 1000
    elif step >= 1000 and step < 5001:
        step = 500
    elif step >= 5001 and step < 10001:
        step = 1000

    result = []
    for n, i in enumerate(range(0, int(pmax), step)):
        if i > pmax:
            break
        min = i + 1
        max = i + step
        products = lfs.catalog.models.Product.objects.filter(effective_price__range=(min, max), pk__in=product_ids)
        result.append({
            "min": min,
            "max": max,
            "quantity": len(products),
        })

    # return result

    new_result = []
    for n, f in enumerate(result):
        if f["quantity"] == 0:
            try:
                result[n + 1]["min"] = f["min"]
            except IndexError:
                pass
            continue
        new_result.append(f)

    return {
        "show_reset": False,
        "show_quantity": True,
        "items": new_result,
    }


def get_product_filters(category, product_filter, price_filter, sorting):
    """Returns the next product filters based on products which are in the given
    category and within the result set of the current filters.
    """
    if price_filter:
        ck_price_filter = "%s|%s" % (price_filter["min"], price_filter["max"])
    else:
        ck_price_filter = ""

    if product_filter:
        ck_product_filter = ""
        for pf in product_filter:
            ck_product_filter += pf[0] + "|"
            ck_product_filter += "|".join(pf[1])
    else:
        ck_product_filter = ""

    cache_key = "%s-productfilters-%s-%s-%s-%s-%s" % (settings.CACHE_MIDDLEWARE_KEY_PREFIX,
        category.slug, ck_product_filter, ck_price_filter, sorting, translation.get_language())

    result = cache.get(cache_key)
    if result is not None:
        return result

    properties_mapping = get_property_mapping()
    options_mapping = get_option_mapping()

    # The base for the calulation of the next filters are the filtered products
    products = get_filtered_products_for_category(
        category, product_filter, price_filter, sorting)
    if not products:
        return []

    # get products and their variants
    product_ids_raw = list(products.values_list('id', flat=True))
    product_ids_raw.extend(lfs.catalog.models.Product.objects.filter(parent__in=products, active=True).values_list('id', flat=True))
    product_ids = ', '.join(map(str, product_ids_raw))

    # Create dict out of already set filters
    set_filters = dict(product_filter)

    property_ids_raw = lfs.catalog.models.ProductPropertyValue.objects.distinct().values_list('property_id', flat=True)
    property_ids = ', '.join(map(str, property_ids_raw))

    # if there is either no products or no property ids there can also be no
    # product filters.
    if not product_ids or not property_ids:
        return []

    result = []
    ########## Number Fields ###################################################

    cursor = connection.cursor()
    cursor.execute("""SELECT property_id, min(value_as_float), max(value_as_float)
                      FROM catalog_productpropertyvalue
                      WHERE type=%s
                      AND product_id IN (%s)
                      AND property_id IN (%s)
                      GROUP BY property_id""" % (PROPERTY_VALUE_TYPE_FILTER, product_ids, property_ids))

    for row in cursor.fetchall():
        prop = properties_mapping[row[0]]

        if not prop.is_number_field or not prop.filterable:
            continue

        # If the filter for a property is already set, we display only the
        # set filter.
        if str(row[0]) in set_filters.keys():
            values = set_filters[str(row[0])]
            result.append({
                "id": row[0],
                "position": prop.position,
                "object": prop,
                "name": prop.name,
                "title": prop.title,
                "unit": prop.unit,
                "items": [{"min": float(values[0]), "max": float(values[1])}],
                "show_reset": True,
                "show_quantity": False,
            })
            continue

        # Otherwise we display all steps.
        items = _calculate_steps(product_ids, prop, row[1], row[2])

        result.append({
            "id": row[0],
            "position": prop.position,
            "object": prop,
            "name": prop.name,
            "title": prop.title,
            "unit": prop.unit,
            "show_reset": False,
            "show_quantity": True,
            "items": items,
        })

    ########## Select and Text Fields ###################################################
    # Count entries for current filter
    # cursor = connection.cursor()
    # cursor.execute("""SELECT property_id, value, parent_id
    #                   FROM catalog_productpropertyvalue
    #                   WHERE type=%s
    #                   AND product_id IN (%s)
    #                   AND property_id IN (%s)""" % (PROPERTY_VALUE_TYPE_FILTER, product_ids, property_ids))
    ppvs = lfs.catalog.models.ProductPropertyValue.objects.filter(type=PROPERTY_VALUE_TYPE_FILTER,
                                               product_id__in=product_ids_raw,
                                               property_id__in=property_ids_raw)

    already_count = {}
    amount = {}
    for ppv in ppvs:
        # We count a property/value pair just one time per *product*. For
        # "products with variants" this could be stored several times within the
        # catalog_productpropertyvalue. Imagine a variant with two properties
        # color and size:
        #   v1 = color:red / size: s
        #   v2 = color:red / size: l
        # But we want to count color:red just one time. As the product with
        # variants is displayed at not the variants.

        if "%s%s%s" % (ppv.parent_id, ppv.property_id, ppv.value) in already_count:
            continue
        already_count["%s%s%s" % (ppv.parent_id, ppv.property_id, ppv.value)] = 1

        if ppv.property_id not in amount:
            amount[ppv.property_id] = {}

        if ppv.value not in amount[ppv.property_id]:
            amount[ppv.property_id][ppv.value] = 0

        amount[ppv.property_id][ppv.value] += 1

    # Group properties and values (for displaying)
    set_filters = dict(product_filter)
    properties = {}
    already_count = []
    for ppv in ppvs:
        prop = ppv.property

        if prop.is_number_field or not prop.filterable or not ppv.value:
            continue

        key = '%s%s' % (ppv.property_id, ppv.value)
        if key in already_count:
            continue
        already_count.append(key)

        if ppv.property_id in properties:
            properties[ppv.property_id] = []

        # If the property is a select field we want to display the name of the
        # option instead of the id.
        position = 1
        if prop.is_select_field:
            try:
                name = options_mapping[ppv.value].name
                position = options_mapping[ppv.value].position
            except KeyError:
                name = ppv.value
        else:
            name = ppv.value

        value = ppv.value

        # if the property within the set filters we just show the selected value
        if str(ppv.property_id) in set_filters.keys():
            if str(ppv.value) in set_filters.values():
                properties[ppv.property_id] = [{
                    "id": ppv.property_id,
                    "value": value,
                    "name": name,
                    "position": position,
                    "quantity": amount[ppv.property_id][ppv.value],
                    "show_quantity": False,
                }]
            continue
        else:
            if not ppv.property_id in properties:
                properties[ppv.property_id] = []
            properties[ppv.property_id].append({
                "id": ppv.property_id,
                "value": value,
                "name": name,
                "position": position,
                "quantity": amount[ppv.property_id][ppv.value],
                "show_quantity": True,
            })

    # Transform the group properties into a list of dicts
    set_filter_keys = set_filters.keys()

    for property_id, values in properties.items():

        prop = properties_mapping[property_id]

        # Sort the values. NOTE: This has to be done here (and not via SQL) as
        # the value field of the property is a char field and can't ordered
        # properly for numbers.
        values.sort(lambda a, b: cmp(a["position"], b["position"]))

        result.append({
            "id": property_id,
            "position": prop.position,
            "unit": prop.unit,
            "show_reset": str(property_id) in set_filter_keys,
            "name": prop.name,
            "title": prop.title,
            "items": values,
        })

    result.sort(lambda a, b: cmp(a["position"], b["position"]))
    cache.set(cache_key, result)

    return result


# TODO: Implement this as a method of Category
def get_filtered_products_for_category(category, filters, price_filter, sorting):
    """Returns products for given categories and current filters sorted by
    current sorting.
    """
    trans_value = build_localized_fieldname('value', translation.get_language())
    langs = get_languages_list()

    if filters:
        if category.show_all_products:
            products = category.get_all_products()
        else:
            products = category.get_products()

        # Generate ids for collected products
        product_ids = ", ".join(map(str, products.values_list('id', flat=True)))

        # Generate filter
        temp = []
        for f in filters:
            if not isinstance(f[1], (list, tuple)):
                trans_filter = []
                for lang in langs:
                    trans_filter.append("%s='%s'" % (build_localized_fieldname('value', lang), f[1]))
                temp.append("property_id='%s' AND (%s)" % (f[0], ' OR '.join(trans_filter)))
            else:
                temp.append("property_id='%s' AND value_as_float BETWEEN '%s' AND '%s'" % (f[0], f[1][0], f[1][1]))

        fstr = " OR ".join(temp)

        # TODO: Will this work with every DB?

        # Get all product ids with matching filters. The idea behind this SQL
        # query is: If for every filter (property=value) for a product id exists
        # a "product property value" the product matches.
        cursor = connection.cursor()
        cursor.execute("""
            SELECT product_id, count(*)
            FROM catalog_productpropertyvalue
            WHERE product_id IN (%s) and (%s) and type=%s
            GROUP BY product_id
            HAVING count(*)=%s""" % (product_ids, fstr, PROPERTY_VALUE_TYPE_FILTER, len(filters)))

        matched_product_ids = [row[0] for row in cursor.fetchall()]

        # All variants of category products
        all_variants = lfs.catalog.models.Product.objects.filter(parent__in=products)

        if all_variants:
            all_variant_ids = all_variants.values_list('id', flat=True)
            all_variant_ids = ', '.join(map(str, all_variant_ids))

            # Variants with matching filters
            cursor.execute("""
                SELECT product_id, count(*)
                FROM catalog_productpropertyvalue
                WHERE product_id IN (%s) and %s and type=%s
                GROUP BY product_id
                HAVING count(*)=%s""" % (all_variant_ids, fstr, PROPERTY_VALUE_TYPE_FILTER, len(filters)))

            # Get the parent ids of the variants as the "product with variants"
            # should be displayed and not the variants.
            variant_ids = [str(row[0]) for row in cursor.fetchall()]
            if variant_ids:
                variant_ids = ", ".join(variant_ids)

                cursor.execute("""
                    SELECT parent_id
                    FROM catalog_product
                    WHERE id IN (%s)""" % variant_ids)

                parent_ids = [str(row[0]) for row in cursor.fetchall()]
                matched_product_ids.extend(parent_ids)

        # As we factored out the ids of all matching products now, we get the
        # product instances in the correct order
        products = lfs.catalog.models.Product.objects.filter(pk__in=matched_product_ids).distinct()
    else:
        categories = [category]
        if category.show_all_products:
            categories.extend(category.get_all_children())
        products = lfs.catalog.models.Product.objects.filter(
            active=True,
            categories__in=categories,
            sub_type__in=[STANDARD_PRODUCT, PRODUCT_WITH_VARIANTS, CONFIGURABLE_PRODUCT]).distinct()

    if price_filter:
        matched_product_ids = []

        # Get all variants of the products
        variants = lfs.catalog.models.Product.objects.filter(parent__in=products)

        # Filter the variants by price
        variants = variants.filter(effective_price__range=[price_filter["min"], price_filter["max"]])

        # Get the parent ids of the variants as the "product with variants"
        # should be displayed and not the variants.
        if variants:
            variant_ids = variants.values_list('id', flat=True)
            variant_ids = ', '.join(map(str, variant_ids))

            cursor = connection.cursor()
            cursor.execute("""
                SELECT parent_id
                FROM catalog_product
                WHERE id IN (%s)""" % variant_ids)

            parent_ids = [str(row[0]) for row in cursor.fetchall()]
            matched_product_ids.extend(parent_ids)

        # Filter the products
        products = products.filter(effective_price__range=[price_filter["min"], price_filter["max"]])

        # Merge the results
        matched_product_ids.extend([p.id for p in products])

        # And get a new query set of all products
        products = lfs.catalog.models.Product.objects.filter(pk__in=matched_product_ids)

    if sorting:
        try:
            products = products.order_by(sorting)
        except FieldError:
            # ignore invalid sort order which may be stored in the session
            pass

    return products


def get_option_mapping():
    """Returns a dictionary with option id to property name.
    """
    options = {}
    for option in lfs.catalog.models.PropertyOption.objects.all():
        options[str(option.id)] = option
    return options


def get_property_mapping():
    """Returns a dictionary with property id to property name.
    """
    properties = {}
    for property in lfs.catalog.models.Property.objects.all():
        properties[property.id] = property

    return properties


def _calculate_steps(product_ids, property, min, max):
    """Calculates filter steps.

    **Parameters**

    product_ids
        The product_ids for which the steps are calculated. List of ids.

    property
        The property for which the steps are calculated. Instance of Property.

    min / max
        The min and max value of all steps. Must be a Float.

    """
    try:
        min = float(min)
        max = float(max)
    except TypeError:
        return []

    result = []

    filter_steps = lfs.catalog.models.FilterStep.objects.filter(property=property.id)
    if property.is_steps_step_type:
        for i, step in enumerate(filter_steps[:len(filter_steps) - 1]):
            min = step.start
            if i != 0:
                min += 1.0
            max = filter_steps[i + 1].start

            result.append({
                "min": min,
                "max": max,
                "quantity": _calculate_quantity(product_ids, property.id, min, max)
            })
    else:
        if property.is_automatic_step_type:
            if max == min:
                step = max
            else:
                diff = max - min
                step = diff / 3         # TODO: Should this be variable?

            if step >= 0 and step < 2:
                step = 1
            elif step >= 2 and step < 6:
                step = 5
            elif step >= 6 and step < 11:
                step = 10
            elif step >= 11 and step < 51:
                step = 50
            elif step >= 51 and step < 101:
                step = 100
            elif step >= 101 and step < 501:
                step = 500
            elif step >= 501 and step < 1001:
                step = 1000
            elif step >= 1000 and step < 5001:
                step = 500
            elif step >= 5001 and step < 10001:
                step = 1000
        else:
            step = property.step

        for n, i in enumerate(range(0, int(max), step)):
            if i > max:
                break
            min = i + 1
            max = i + step

            result.append({
                "min": min,
                "max": max,
                "quantity": _calculate_quantity(product_ids, property.id, min, max),
            })

    if property.display_no_results:
        return result
    else:
        # Remove entries with zero products
        new_result = []
        for n, f in enumerate(result):
            if f["quantity"] == 0:
                try:
                    result[n + 1]["min"] = f["min"]
                except IndexError:
                    pass
                continue
            new_result.append(f)

        return new_result


def _calculate_quantity(product_ids, property_id, min, max):
    """Calculate the amount of products for given parameters.
    """
    trans_value = build_localized_fieldname('value', translation.get_language())
    # Count entries for current filter
    cursor = connection.cursor()
    cursor.execute("""SELECT property_id, %s, parent_id
                      FROM catalog_productpropertyvalue
                      WHERE product_id IN (%s)
                      AND property_id = %s
                      AND value_as_float BETWEEN %s AND %s""" % (trans_value, product_ids, property_id, min, max))

    already_count = {}
    amount = 0
    for row in cursor.fetchall():
        # We count a property/value pair just one time per *product*. For
        # "products with variants" this could be stored several times within the
        # catalog_productpropertyvalue. Imagine a variant with two properties
        # color and size:
        #   v1 = color:red / size: s
        #   v2 = color:red / size: l
        # But we want to count color:red just one time. As the product with
        # variants is displayed at not the variants.

        if "%s%s%s" % (row[2], row[0], row[1]) in already_count:
            continue
        already_count["%s%s%s" % (row[2], row[0], row[1])] = 1

        amount += 1

    return amount
