from django import forms
from lfs.core.translation_utils import prepare_fields_order
from lfs.portlet.models import RecentProductsPortlet


class RecentProductsForm(forms.ModelForm):
    """Form for the RecentProductsPortlet.
    """
    def __init__(self, *args, **kwargs):
        super(RecentProductsForm, self).__init__(*args, **kwargs)
        prepare_fields_order(self)

    class Meta:
        model = RecentProductsPortlet

