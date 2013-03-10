# django imports
from django.forms import ModelForm

# lfs imports
from lfs.core.translation_utils import prepare_fields_order
from lfs.core.widgets.image import LFSImageInput
from lfs.manufacturer.models import Manufacturer


class ManufacturerAddForm(ModelForm):
    """Process form to add a manufacturer.
    """
    class Meta:
        model = Manufacturer
        fields = ("name", "slug")


class ManufacturerDataForm(ModelForm):
    """Form to manage selection data.
    """
    def __init__(self, *args, **kwargs):
        super(ManufacturerDataForm, self).__init__(*args, **kwargs)
        self.fields["image"].widget = LFSImageInput()
        prepare_fields_order(self, fields=("name", "slug", "short_description", "description", "image"))

    class Meta:
        model = Manufacturer


class ViewForm(ModelForm):
    """Form to add/edit category.
    """
    class Meta:
        model = Manufacturer
        fields = ("active_formats", "product_cols", "product_rows", )
