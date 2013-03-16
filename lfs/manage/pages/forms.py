# django imports
from django.forms import ModelForm, ValidationError
from django.utils.translation import ugettext_lazy as _

# lfs imports
from lfs.core.widgets.file import LFSFileInput
from lfs.page.models import Page
from lfs.core.translation_utils import prepare_fields_order, get_translation_fields, uses_modeltranslation


class PageAddForm(ModelForm):
    """Form to add a page.
    """
    def __init__(self, *args, **kwargs):
        # get fields from kwargs as we're using this form as a base for edit form too
        fields = ('title', 'slug')
        if 'fields' in kwargs:
            fields = kwargs.get('fields')
            del kwargs['fields']

        super(PageAddForm, self).__init__(*args, **kwargs)

        prepare_fields_order(self, fields=fields)
        if not uses_modeltranslation():
            # require slug field
            self.fields['slug'].required = True

    def clean(self):
        """ If translations are used then at least one title and one slug are required
        """
        cleaned_data = super(PageAddForm, self).clean()

        # at least one name and one slug has to be defined
        if uses_modeltranslation():
            slug_fields = get_translation_fields('slug')
            title_fields = get_translation_fields('title')

            values_title = [self.cleaned_data.get(trans_name, '') for trans_name in title_fields]
            values_slug = [self.cleaned_data.get(trans_name, '') for trans_name in slug_fields]

            if not any(values_title):
                raise ValidationError(_('At least one title has to be defined'))

            if not any(values_slug):
                raise ValidationError(_('At least one slug has to be defined'))

            # check for uniqueness
            for slug_field_name in slug_fields:
                val = self.cleaned_data.get(slug_field_name).strip()
                if val:
                    qs = self._meta.model.objects.filter(**{slug_field_name: val})
                    if self.instance.pk:
                        qs = qs.exclude(pk=self.instance.pk)
                    if qs.exists():
                        msg = _(u"Slug '%s' already exists!") % val
                        self._errors[slug_field_name] = self.error_class([msg])
                        del cleaned_data[slug_field_name]
        return cleaned_data

    class Meta:
        model = Page


class PageForm(PageAddForm):
    """Form to edit a page.
    """
    def __init__(self, *args, **kwargs):
        kwargs['fields'] = ('active', 'title', 'slug', 'exclude_from_navigation', 'short_text', 'body', 'file')
        super(PageForm, self).__init__(*args, **kwargs)
        if uses_modeltranslation():
            for fname in get_translation_fields('file'):
                self.fields[fname].widget = LFSFileInput()
        else:
            self.fields["file"].widget = LFSFileInput()

    class Meta:
        model = Page
