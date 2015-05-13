# django imports
from django.forms import ModelForm

# lfs imports
from lfs.core.widgets.image import LFSImageInput
from lfs.shipping.models import ShippingMethod
from lfs.core.translation_utils import prepare_fields_order


class ShippingMethodAddForm(ModelForm):
    """Form to add a shipping method.
    """
    def __init__(self, *args, **kwargs):
        super(ShippingMethodAddForm, self).__init__(*args, **kwargs)
        prepare_fields_order(self, fields=('name', ))

    class Meta:
        model = ShippingMethod
        fields = ("name",)


class ShippingMethodForm(ModelForm):
    """
    """
    def __init__(self, *args, **kwargs):
        super(ShippingMethodForm, self).__init__(*args, **kwargs)
        self.fields["image"].widget = LFSImageInput()
        prepare_fields_order(self, exclude=('priority', ))

    class Meta:
        model = ShippingMethod
        exclude = ("priority",)
