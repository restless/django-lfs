from lfs.core.translation_utils import uses_modeltranslation

if uses_modeltranslation():
    from modeltranslation.translator import translator, TranslationOptions
    from .models import PaymentMethod


    class PaymentMethodTranslationOptions(TranslationOptions):
        fields = ('name', 'description', 'note')

    translator.register(PaymentMethod, PaymentMethodTranslationOptions)
