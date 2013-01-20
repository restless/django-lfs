# -*- coding: utf-8 -*-
from django.conf import settings

try:
    from modeltranslation.utils import get_translation_fields, build_localized_fieldname
    from modeltranslation.manager import get_translatable_fields_for_model
except ImportError:
    def get_translation_fields(field):
        return [field]

    def build_localized_fieldname(field, l):
        return field

    def get_translatable_fields_for_model(cls):
        return {}


def prepare_fields_order(form, *fields):
    """ return list of field names expanding it with translated field names if modeltranslation is in use
    """
    out = []
    for field in fields:
        trans_dict = get_translatable_fields_for_model(form.instance.__class__)
        out.extend(trans_dict.get(field, [field]))
    return out


def get_languages_list():
    """ Returns language codes as list
        Don't use cache here as it locks itself!
    """
    langs = getattr(settings, 'LANGUAGES_LIST', None)
    if not langs:
        langs = [language[0] for language in settings.LANGUAGES]
    return langs


def get_default_language():
    try:
        from modeltranslation.settings import DEFAULT_LANGUAGE
    except ImportError:
        DEFAULT_LANGUAGE = settings.LANGUAGE_CODE
    return DEFAULT_LANGUAGE
