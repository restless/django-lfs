from django import forms
from lfs.core.translation_utils import prepare_fields_order
from lfs.portlet.models import TopsellerPortlet


class TopsellerForm(forms.ModelForm):
    """Form for the TopsellerPortlet.
    """
    def __init__(self, *args, **kwargs):
        super(TopsellerForm, self).__init__(*args, **kwargs)
        prepare_fields_order(self)

    class Meta:
        model = TopsellerPortlet
        exclude = ()
