from django import forms
from lfs.core.translation_utils import prepare_fields_order
from lfs.portlet.models import PagesPortlet


class PagesForm(forms.ModelForm):
    """Form for the PagesPortlet.
    """
    def __init__(self, *args, **kwargs):
        super(PagesForm, self).__init__(*args, **kwargs)
        prepare_fields_order(self)

    class Meta:
        model = PagesPortlet
