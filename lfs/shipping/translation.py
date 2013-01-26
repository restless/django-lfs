try:
    from modeltranslation.translator import translator, TranslationOptions
    from .models import ShippingMethod


    class ShippingMethodTranslationOptions(TranslationOptions):
        fields = ('name', 'description', 'note')

    translator.register(ShippingMethod, ShippingMethodTranslationOptions)
except ImportError:
    pass
