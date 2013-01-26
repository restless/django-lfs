try:
    from modeltranslation.translator import translator, TranslationOptions
    from .models import PaymentMethod


    class PaymentMethodTranslationOptions(TranslationOptions):
        fields = ('name', 'description', 'note')

    translator.register(PaymentMethod, PaymentMethodTranslationOptions)
except ImportError:
    pass
