from lfs.core.translation_utils import uses_modeltranslation

if uses_modeltranslation():
    from modeltranslation.translator import translator, TranslationOptions
    from .models import Manufacturer

    # manufacturer
    class ManufacturerTranslationOptions(TranslationOptions):
        fields = ('short_description', 'description', 'meta_title', 'meta_keywords', 'meta_description')

    translator.register(Manufacturer, ManufacturerTranslationOptions)