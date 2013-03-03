from django import forms
from lfs.core.translation_utils import prepare_fields_order
from lfs.portlet.models import TextPortlet


class TextPortletForm(forms.ModelForm):
    """Form for the TextPortlet.
    """
    def __init__(self, *args, **kwargs):
        super(TextPortletForm, self).__init__(*args, **kwargs)
        prepare_fields_order(self)

    class Meta:
        model = TextPortlet