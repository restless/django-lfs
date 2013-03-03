try:
    from modeltranslation.translator import translator, TranslationOptions
    from .models import Action, Country, Shop


    class ActionTranslationOptions(TranslationOptions):
        fields = ('title', 'link')

    translator.register(Action, ActionTranslationOptions)

    class CountryTranslationOptions(TranslationOptions):
        fields = ('name', )

    class ShopTranslationOptions(TranslationOptions):
        fields = ('name', 'description', 'image', 'meta_title', 'meta_keywords', 'meta_description')

    translator.register(Shop, ShopTranslationOptions)
except ImportError:
    pass
