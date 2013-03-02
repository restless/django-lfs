try:
    from modeltranslation.translator import translator, TranslationOptions
    from .models import Action, Country


    class ActionTranslationOptions(TranslationOptions):
        fields = ('title', 'link')

    translator.register(Action, ActionTranslationOptions)

    class CountryTranslationOptions(TranslationOptions):
        fields = ('name', )

    translator.register(Country, CountryTranslationOptions)
except ImportError:
    pass
