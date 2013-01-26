try:
    from modeltranslation.translator import translator, TranslationOptions
    from .models import Category, DeliveryTime


    class CategoryTranslationOptions(TranslationOptions):
        fields = ('name', 'slug', 'short_description', 'description', 'meta_title', 'meta_keywords', 'meta_description', 'image')

    translator.register(Category, CategoryTranslationOptions)

    class DeliveryTimeTranslationOptions(TranslationOptions):
            fields = ('description',)

    translator.register(DeliveryTime, DeliveryTimeTranslationOptions)
except ImportError:
    pass
