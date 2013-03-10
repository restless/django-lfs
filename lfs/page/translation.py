from lfs.core.translation_utils import uses_modeltranslation

if uses_modeltranslation():
    from modeltranslation.translator import translator, TranslationOptions
    from .models import Page

    class PageTranslationOptions(TranslationOptions):
        fields = ('title', 'slug', 'short_text', 'body', 'meta_title', 'meta_keywords', 'meta_description', 'file')

    translator.register(Page, PageTranslationOptions)
