from django import forms
from lfs.core.translation_utils import prepare_fields_order
from lfs.portlet.models import CartPortlet

class CartPortletForm(forms.ModelForm):
    """Form for CartPortlet.
    """
    def __init__(self, *args, **kwargs):
        super(CartPortletForm, self).__init__(*args, **kwargs)
        prepare_fields_order(self)

    class Meta:
        model = CartPortlet