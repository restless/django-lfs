# -*- coding: utf-8 -*-
from django.conf import settings
from django.forms.models import fields_for_model

try:
    from localeurl.models import reverse
except ImportError:
    from django.core.urlresolvers import reverse


def get_translation_fields(field):
    return [field]


def build_localized_fieldname(field, l):
    return field


def get_translatable_fields_for_model(cls):
    return {}


def uses_modeltranslation():
    if 'modeltranslation' in settings.INSTALLED_APPS:
        return True
    return False


AVAILABLE_LANGUAGES = [language[0] for language in settings.LANGUAGES]

if uses_modeltranslation():
    try:
        from modeltranslation.utils import get_translation_fields, build_localized_fieldname
        from modeltranslation.manager import get_translatable_fields_for_model
        from modeltranslation import settings as modeltranslation_settings
        AVAILABLE_LANGUAGES = modeltranslation_settings.AVAILABLE_LANGUAGES
    except ImportError:
        pass


def prepare_fields_order(form, fields=None, exclude=None):
    """ Replace fields with their translated counterparts, eg:
        if slug and name are marked for translation
        fields = ['slug', 'name', 'is_active']
        will be:
        fields = ['slug_en', 'slug_de', 'name_en', 'name_de', 'is_active']
    """
    trans_dict = get_translatable_fields_for_model(form.instance.__class__)
    out = []  # sort order

    if not fields:
        fields = fields_for_model(form.instance, exclude=exclude).keys()

    if trans_dict:
        for field in fields:
            trans_fields = trans_dict.get(field, [field])
            out.extend(trans_fields)
            if len(trans_fields) > 1 and field in form.fields:
                form.fields.pop(field)
    else:
        out = fields

    form.fields.keyOrder = out
    return out


def get_languages_list():
    """ Returns language codes as list
        Don't use cache here as it locks itself!
    """
    if uses_modeltranslation():
        return AVAILABLE_LANGUAGES
    return [settings.LANGUAGE_CODE]


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
