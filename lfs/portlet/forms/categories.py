from django import forms
from lfs.core.translation_utils import prepare_fields_order
from lfs.portlet.models import CategoriesPortlet


class CategoriesPortletForm(forms.ModelForm):
    """Form for CategoriesPortlet.
    """
    def __init__(self, *args, **kwargs):
        super(CategoriesPortletForm, self).__init__(*args, **kwargs)
        prepare_fields_order(self)

    class Meta:
        model = CategoriesPortlet
        exclude = ()
