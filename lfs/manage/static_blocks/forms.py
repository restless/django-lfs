# django imports
from django.forms import ModelForm
from django.forms import ModelForm, ValidationError
from django.utils.translation import ugettext_lazy as _

# lfs imports
from lfs.catalog.models import StaticBlock
from lfs.core.translation_utils import prepare_fields_order, get_translation_fields, uses_modeltranslation

class StaticBlockForm(ModelForm):
    """
    Form to add and edit a static block.
    """
    def __init__(self, *args, **kwargs):
        super(StaticBlockForm, self).__init__(*args, **kwargs)
        prepare_fields_order(self, exclude=('position',))

    def clean(self):
        """ If translations are used then at least one name is required
        """
        cleaned_data = super(StaticBlockForm, self).clean()
        name_fields = get_translation_fields('name')

        # at least one name and one slug has to be defined
        if uses_modeltranslation():
            title_fields = get_translation_fields('title')

            values_name = [self.cleaned_data.get(trans_name, '') for trans_name in name_fields]

            if not any(values_name):
                raise ValidationError(_('At least one name has to be defined'))

        # check for uniqueness
        for fname in name_fields:
            val = self.cleaned_data.get(fname).strip()
            if val:
                qs = self._meta.model.objects.filter(**{fname: val})
                if self.instance.pk:
                    qs = qs.exclude(pk=self.instance.pk)
                if qs.exists():
                    msg = _(u"Name '%s' already exists!") % val
                    self._errors[fname] = self.error_class([msg])
                    del cleaned_data[fname]

        return cleaned_data

    class Meta:
        model = StaticBlock
