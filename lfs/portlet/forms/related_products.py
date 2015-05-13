from django import forms
from lfs.core.translation_utils import prepare_fields_order
from lfs.portlet.models import RelatedProductsPortlet


class RelatedProductsForm(forms.ModelForm):
    """Form for the RelatedProductsPortlet.
    """
    def __init__(self, *args, **kwargs):
        super(RelatedProductsForm, self).__init__(*args, **kwargs)
        prepare_fields_order(self)

    class Meta:
        model = RelatedProductsPortlet
        exclude = ()
