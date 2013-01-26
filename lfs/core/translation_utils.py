# -*- coding: utf-8 -*-
from django.conf import settings
from django.forms.models import fields_for_model
from django.core.urlresolvers import reverse

try:
    from modeltranslation.utils import get_translation_fields, build_localized_fieldname
    from modeltranslation.manager import get_translatable_fields_for_model
    from modeltranslation import settings as modeltranslation_settings
    AVAILABLE_LANGUAGES = modeltranslation_settings.AVAILABLE_LANGUAGES
except ImportError:
    def get_translation_fields(field):
        return [field]

    def build_localized_fieldname(field, l):
        return field

    def get_translatable_fields_for_model(cls):
        return {}

    AVAILABLE_LANGUAGES = [language[0] for language in settings.LANGUAGES]


def prepare_fields_order(form, fields=None, exclude=None):
    """ return list of field names expanding it with translated field names if modeltranslation is in use
    """
    trans_dict = get_translatable_fields_for_model(form.instance.__class__)
    out = []
    if not fields:
        out = fields_for_model(form.instance, exclude=exclude).keys()
        if trans_dict:
            for key in trans_dict.keys():
                out.remove(key)
    else:
        for field in fields:
            out.extend(trans_dict.get(field, [field]))
    form.fields.keyOrder = out
    return out


def get_languages_list():
    """ Returns language codes as list
        Don't use cache here as it locks itself!
    """
    return AVAILABLE_LANGUAGES


def get_default_language():
    try:
        from modeltranslation.settings import DEFAULT_LANGUAGE
    except ImportError:
        DEFAULT_LANGUAGE = settings.LANGUAGE_CODE
    return DEFAULT_LANGUAGE


def lfs_reverse(*args, **kwargs):
    if not 'localeurl' in settings.INSTALLED_APPS:
        del kwargs['locale']
    return reverse(*args, **kwargs)
