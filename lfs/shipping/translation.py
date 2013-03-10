from lfs.core.translation_utils import uses_modeltranslation

if uses_modeltranslation():
    from modeltranslation.translator import translator, TranslationOptions
    from .models import ShippingMethod


    class ShippingMethodTranslationOptions(TranslationOptions):
        fields = ('name', 'description', 'note')

    translator.register(ShippingMethod, ShippingMethodTranslationOptions)
