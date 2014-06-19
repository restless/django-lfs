# django imports
from django.forms import ModelForm, ValidationError
from django.utils.translation import ugettext_lazy as _

# lfs imports
from lfs.catalog.models import Property, PropertyOption
from lfs.core.translation_utils import prepare_fields_order, get_translation_fields, uses_modeltranslation


class PropertyAddForm(ModelForm):
    """Form to add a property.
    """
    def __init__(self, *args, **kwargs):
        super(PropertyAddForm, self).__init__(*args, **kwargs)
        prepare_fields_order(self, fields=("name", ))

    class Meta:
        model = Property


class PropertyDataForm(ModelForm):
    """Form to manage core data of a property.
    """
    def __init__(self, *args, **kwargs):
        super(PropertyDataForm, self).__init__(*args, **kwargs)
        prepare_fields_order(self, fields=("position", "name", "title", "unit", "variants", "filterable",
                                           "configurable", "required", "display_on_product"))
        
    def clean(self):
        """ If translations are used then at least one name is required
        """
        cleaned_data = super(PropertyDataForm, self).clean()
        title_fields = get_translation_fields('title')
        name_fields = get_translation_fields('name')

        # at least one name and one title has to be defined
        if uses_modeltranslation():
            values_title = [self.cleaned_data.get(trans_name, '') for trans_name in title_fields]
            values_name = [self.cleaned_data.get(trans_name, '') for trans_name in name_fields]

            if not any(values_title):
                raise ValidationError(_('At least one title has to be defined'))

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
        model = Property


class PropertyTypeForm(ModelForm):
    """Form to manage property type.
    """
    class Meta:
        model = Property
        fields = ["type"]


class StepTypeForm(ModelForm):
    """Form to manage the step type of a property.
    """
    class Meta:
        model = Property
        fields = ["step_type"]


class SelectFieldForm(ModelForm):
    """Form to manage attributes for select field.
    """
    class Meta:
        model = Property
        fields = ["display_price", "add_price"]


class NumberFieldForm(ModelForm):
    """Form to manage the number field.
    """
    class Meta:
        model = Property
        fields = ["decimal_places", "unit_min", "unit_max", "unit_step"]


class StepRangeForm(ModelForm):
    """Form to manage step range.
    """
    class Meta:
        model = Property
        fields = ["step"]


class PropertyOptionForm(ModelForm):
    """Form to add a property option.
    """
    def __init__(self, *args, **kwargs):
        super(PropertyOptionForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:
            self.initial['position'] = ''
        self.fields['position'].widget.attrs = {'class': 'number', 'size': 3}
        self.fields['position'].required = False
        prepare_fields_order(self, fields=("position", "name", "price"))

    def clean(self):
        """ If translations are used then at least one name is required
        """
        cleaned_data = super(PropertyOptionForm, self).clean()
        if not cleaned_data.get('position', ''):
            self.cleaned_data['position'] = 99
        name_fields = get_translation_fields('name')

        # at least one name has to be defined
        if uses_modeltranslation():
            values_name = [self.cleaned_data.get(trans_name, '') for trans_name in name_fields]

            if not any(values_name):
                raise ValidationError(_('At least one name has to be defined'))

        return cleaned_data

    class Meta:
        model = PropertyOption
