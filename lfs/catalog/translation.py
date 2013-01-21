from modeltranslation.translator import translator, TranslationOptions
from .models import Category


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug', 'short_description', 'description', 'meta_keywords', 'meta_description', 'image')

translator.register(Category, CategoryTranslationOptions)
