from django import forms
from lfs.core.translation_utils import prepare_fields_order
from lfs.portlet.models import FilterPortlet


class FilterPortletForm(forms.ModelForm):
    """Form for the FilterPortlet.
    """
    def __init__(self, *args, **kwargs):
        super(FilterPortletForm, self).__init__(*args, **kwargs)
        prepare_fields_order(self)

    class Meta:
        model = FilterPortlet
        exclude = ()
