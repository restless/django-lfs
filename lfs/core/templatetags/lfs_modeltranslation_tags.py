# -*- coding: utf-8 -*-
from django.template import Library
from django import template
from django.utils.safestring import mark_safe
from django.utils import translation
from django.conf import settings

from lfs.core.translation_utils import (get_translation_fields, build_localized_fieldname, get_languages_list,
                                        get_default_language, uses_modeltranslation)

register = Library()


class NTFieldsNode(template.Node):
    def __init__(self, form, field_name, nodelist):
        self.form = template.Variable(form)
        self.field_name = template.Variable(field_name)
        self.request = template.Variable('request')
        self.nodelist = nodelist

    def render(self, context):
        """ prepare list of translation fields (Form) for specific field name
        """
        form = self.form.resolve(context)
        field_name = self.field_name.resolve(context)

        out = [form[tname] for tname in get_translation_fields(field_name)]
        context['%s_translations' % field_name] = out

        default_language = get_default_language()

        uses_translation = uses_modeltranslation()

        output = []
        for lang in get_languages_list():
            tname = build_localized_fieldname(field_name, lang)
            context['translated_field'] = form[tname]
            context['translation_language'] = lang
            if lang == default_language:
                context['translation_default_language'] = True
                context['uses_modeltranlsation'] = uses_translation
                setattr(context['translated_field'], 'default_language', True)
                attrs = context['translated_field'].field.widget.attrs
                if not attrs:
                    attrs = {}
                css_classes = attrs.get('class', '').split(' ')
                css_classes.append('default_language')
                attrs['class'] = ' '.join(css_classes).strip()
                context['translated_field'].field.widget.attrs = attrs
            output.append(self.nodelist.render(context))
        return ''.join(output)


@register.tag(name="translatedfields")
def do_set_translated_fields(parser, token):
    """ Used to render form field for all defined languages:

        {% translatedfiels form "name" %}
            <div {% if translation_default_language %}class="main-language"{% endif %}>
                {{ translated_field.label_tag }}
                {{ translated_field }}
            </div>
        {% endtranslatedfiels %}
    """
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, form, field_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires form and field arguments" % token.contents.split()[0])
    nodelist = parser.parse(('endtranslatedfields',))
    parser.delete_first_token()
    return NTFieldsNode(form, field_name, nodelist)


class NTAttrsNode(template.Node):
    def __init__(self, obj, attr_name, show_empty, nodelist):
        self.obj = template.Variable(obj)
        self.attr_name = template.Variable(attr_name)
        self.show_empty = template.Variable(show_empty)
        self.request = template.Variable('request')
        self.nodelist = nodelist

    def render(self, context):
        """ prepare list of translation attributes for specific attribute/item
        """
        obj = self.obj.resolve(context)
        attr_name = self.attr_name.resolve(context)
        show_empty = self.show_empty.resolve(context)

        default_language = get_default_language()
        uses_translation = uses_modeltranslation()

        output = []
        langs_list = get_languages_list()
        out = []
        for i, lang in enumerate(langs_list):
            ctx = {}
            tname = build_localized_fieldname(attr_name, lang)
            if hasattr(obj, '__getitem__'):
                ctx['translated_attr'] = obj.get(tname, '')
            else:
                ctx['translated_attr'] = getattr(obj, tname, '')
            if not ctx['translated_attr'] and not show_empty:
                continue
            ctx['translation_language'] = lang
            if lang == default_language:
                ctx['translation_default_language'] = True
            ctx['uses_modeltranlsation'] = uses_translation
            out.append(ctx)

        last = len(out) - 1
        for i, ctx in enumerate(out):
            out[i]['fortranslatedattrsloop'] = {'last': i == last, 'first': i == 0, 'count': i}
        for ctx in out:
            context.update(ctx)
            output.append(self.nodelist.render(context))
        return ''.join(output)


@register.tag(name="fortranslatedattrs")
def do_set_translated_attrs(parser, token):
    """ Iterates through all translated versions of specific attribute of object, eg:
        {% fortranslatedattrs obj "slug" 1 %}
           {{ fortranslatedloop.count }}. lang: {{ translation_language }}: {{ translated_attr }}
        {% endfortranslatedattrs %}

        for en, de, pl languages will result in something like:

          1. lang: en: english_value
          2. lang: de: german_value
          3. lang: pl: polish_value

        Parameters:
        obj - object
        attr_name - attribute (or key for dict) name
        show_empty - whether to show or hide empty translations
    """
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, obj, attr_name, show_empty = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires obj, field, show_empty arguments" % token.contents.split()[0])
    nodelist = parser.parse(('endfortranslatedattrs',))
    parser.delete_first_token()
    return NTAttrsNode(obj, attr_name, show_empty, nodelist)


class SwitchLanguageNode(template.Node):
    def __init__(self, language_code, nodelist):
        self.request = template.Variable('request')
        self.language_code = template.Variable(language_code)
        self.nodelist = nodelist

    def render(self, context):
        """ prepare list of translation fields (Form) for specific field name
        """
        language_code = self.language_code.resolve(context)
        current_language = translation.get_language()
        translation.activate(language_code)
        out = self.nodelist.render(context)
        translation.activate(current_language)
        return out


@register.tag(name="switchlanguage")
def do_switch_language(parser, token):
    """ Switch language within tag.
        {% switchlanguage "en" %}
            {% trans "blah" %}
        {% endswitchlanguage %}
    """
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, language_code = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires one argument" % token.contents.split()[0])
    nodelist = parser.parse(('endswitchlanguage',))
    parser.delete_first_token()
    return SwitchLanguageNode(language_code, nodelist)


class NTLanguagesNode(template.Node):
    def __init__(self, nodelist):
        self.request = template.Variable('request')
        self.nodelist = nodelist

    def render(self, context):
        """ render in context of all available languages
        """
        default_language = get_default_language()
        current_language = translation.get_language()

        output = []
        langs_list = get_languages_list()
        out = []
        for i, lang in enumerate(langs_list):
            ctx = dict(translation_language=lang)
            if lang == default_language:
                ctx['translation_default_language'] = True
            out.append(ctx)

        last = len(out) - 1
        for i, ctx in enumerate(out):
            out[i]['forlanguagesloop'] = {'last': i == last, 'first': i == 0, 'count': i}
        for ctx in out:
            translation.activate(ctx['translation_language'])
            context.update(ctx)
            output.append(self.nodelist.render(context))
        translation.activate(current_language)
        return ''.join(output)


@register.tag(name="forlanguages")
def do_for_languages(parser, token):
    """ Iterates through all lanuages and switches context language for each run:
        {% forlanguages %}
           <div>{% trans "I'll be show in all languages" %}</div>
        {% endforlanguages %}
    """
    try:
        # split_contents() knows not to split quoted strings.
        tag_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag takes no arguments" % token.contents.split()[0])
    nodelist = parser.parse(('endforlanguages',))
    parser.delete_first_token()
    return NTLanguagesNode(nodelist)


@register.simple_tag
def get_translation_languages_js():
    langlist = ','.join(["'%s'" % lang for lang in get_languages_list()])
    return mark_safe('var TRANSLATION_LANGUAGES = [%s];' % langlist)


@register.inclusion_tag('lfs/shop/_language_switch_menu.html')
def language_switch_menu():
    languages = [(code, label) for code, label in settings.LANGUAGES]
    return {'uses_modeltranslation': uses_modeltranslation(),
            'languages': languages}