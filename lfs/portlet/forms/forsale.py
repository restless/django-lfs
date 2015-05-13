from django import forms
from lfs.core.translation_utils import prepare_fields_order
from lfs.portlet.models import ForsalePortlet


class ForsaleForm(forms.ModelForm):
    """
    """
    def __init__(self, *args, **kwargs):
        super(ForsaleForm, self).__init__(*args, **kwargs)
        prepare_fields_order(self)

    class Meta:
        model = ForsalePortlet
        exclude = ()
