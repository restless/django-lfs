try:
    from modeltranslation.translator import translator, TranslationOptions
    from .models import Page

    class PageTranslationOptions(TranslationOptions):
        fields = ('title', 'slug', 'short_text', 'body', 'meta_title', 'meta_keywords', 'meta_description', 'file')

    translator.register(Page, PageTranslationOptions)
except ImportError:
    pass
