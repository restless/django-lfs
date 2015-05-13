from lfs.core.translation_utils import uses_modeltranslation
print 'if uses modeltranslation'
if uses_modeltranslation():
    print ' uses modeltranslation'
    from modeltranslation.translator import translator, TranslationOptions
    from .models import Action, Country, Shop, ActionGroup

    class ActionTranslationOptions(TranslationOptions):
        fields = ('title', 'link')
    translator.register(Action, ActionTranslationOptions)

    class CountryTranslationOptions(TranslationOptions):
        fields = ('name', )
    translator.register(Country, CountryTranslationOptions)

    class ShopTranslationOptions(TranslationOptions):
        fields = ('name', 'description', 'image', 'meta_title', 'meta_keywords', 'meta_description')
    translator.register(Shop, ShopTranslationOptions)

    class ActionGroupTranslationOptions(TranslationOptions):
        fields = ('name', )
    translator.register(ActionGroup, ActionGroupTranslationOptions)
