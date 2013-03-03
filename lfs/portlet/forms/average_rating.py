from django import forms
from lfs.core.translation_utils import prepare_fields_order
from lfs.portlet.models import AverageRatingPortlet


class AverageRatingForm(forms.ModelForm):
    """Form for the AverageRatingPortlet.
    """
    def __init__(self, *args, **kwargs):
        super(AverageRatingForm, self).__init__(*args, **kwargs)
        prepare_fields_order(self)

    class Meta:
        model = AverageRatingPortlet