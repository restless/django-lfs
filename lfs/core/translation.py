try:
    from modeltranslation.translator import translator, TranslationOptions
    from .models import Action, ActionGroup


    class ActionTranslationOptions(TranslationOptions):
        fields = ('title', 'link')

    translator.register(Action, ActionTranslationOptions)
except ImportError:
    pass
