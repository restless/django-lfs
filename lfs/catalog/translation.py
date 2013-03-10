from lfs.core.translation_utils import uses_modeltranslation

if uses_modeltranslation():
    from modeltranslation.translator import translator, TranslationOptions
    from .models import Category, DeliveryTime, Product, StaticBlock, Property, PropertyOption, ProductPropertyValue

    # category
    class CategoryTranslationOptions(TranslationOptions):
        fields = ('name', 'slug', 'short_description', 'description', 'meta_title', 'meta_keywords', 'meta_description', 'image')

    translator.register(Category, CategoryTranslationOptions)

    # product
    class ProductTranslationOptions(TranslationOptions):
        fields = ('name', 'slug', 'short_description', 'description', 'meta_title', 'meta_description', 'meta_keywords')

    translator.register(Product, ProductTranslationOptions)

    # delivery
    class DeliveryTimeTranslationOptions(TranslationOptions):
            fields = ('description',)

    translator.register(DeliveryTime, DeliveryTimeTranslationOptions)

    # static block
    class StaticBlockTranslationOptions(TranslationOptions):
            fields = ('name', 'html',)

    translator.register(StaticBlock, StaticBlockTranslationOptions)

    # property
    class PropertyTranslationOptions(TranslationOptions):
            fields = ('name', 'title', )

    translator.register(Property, PropertyTranslationOptions)

    # property option
    class PropertyOptionTranslationOptions(TranslationOptions):
            fields = ('name', )

    translator.register(PropertyOption, PropertyOptionTranslationOptions)

    # product property value
    class ProductPropertyValueTranslationOptions(TranslationOptions):
        fields = ('value', )

    translator.register(ProductPropertyValue, ProductPropertyValueTranslationOptions)
