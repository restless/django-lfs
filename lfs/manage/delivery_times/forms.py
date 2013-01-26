# django imports
from django.forms import ModelForm

# lfs imports
from lfs.catalog.models import DeliveryTime
from lfs.core.translation_utils import prepare_fields_order


class DeliveryTimeAddForm(ModelForm):
    """Form to edit add a delivery time.
    """
    class Meta:
        model = DeliveryTime
        fields = ("min", "max", "unit")


class DeliveryTimeForm(ModelForm):
    """Form to edit a delivery time.
    """
    def __init__(self, *args, **kwargs):
        super(DeliveryTimeForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = prepare_fields_order(self)

    class Meta:
        model = DeliveryTime
