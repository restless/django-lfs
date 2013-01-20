# -*- coding: utf-8 -*-
from django.template import Library
from django import template
from django.utils.safestring import mark_safe

from lfs.core.translation_utils import get_translation_fields, build_localized_fieldname, get_languages_list

register = Library()


class NTFieldsNode(template.Node):
    def __init__(self, form, field_name, nodelist):
        self.form = template.Variable(form)
        self.field_name = template.Variable(field_name)
        self.request = template.Variable('request')
        self.nodelist = nodelist

    def render(self, context):
        """ prepare list of translation fields (Form) for specific field name
        """
        form = self.form.resolve(context)
        field_name = self.field_name.resolve(context)

        out = [form[tname] for tname in get_translation_fields(field_name)]
        context['%s_translations' % field_name] = out

        output = []
        for lang in get_languages_list():
            tname = build_localized_fieldname(field_name, lang)
            import pdb;pdb.set_trace()
            context['tfield'] = form[tname]
            form.fields[field_name].field = form[tname]
            output.append(self.nodelist.render(context))

        return ''.join(output)


@register.tag(name="translatedfields")
def do_set_translated_fields(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, form, field_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    nodelist = parser.parse(('endtranslatedfields',))
    parser.delete_first_token()
    return NTFieldsNode(form, field_name, nodelist)


@register.simple_tag
def get_translation_languages_js():
    langlist = ','.join(["'%s'" % lang for lang in get_languages_list()])
    return mark_safe('var TRANSLATION_LANGUAGES = [%s];' % langlist)
