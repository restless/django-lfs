try:
    from modeltranslation.translator import translator, TranslationOptions
    from .models import Category, DeliveryTime, Product, StaticBlock, Property

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

    # static block
    class PropertyTranslationOptions(TranslationOptions):
            fields = ('name', 'title', )

    translator.register(Property, PropertyTranslationOptions)

except ImportError:
    pass
