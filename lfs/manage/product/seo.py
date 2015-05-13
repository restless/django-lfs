# django imports
from django.forms import ModelForm

# lfs.imports
from lfs.catalog.models import Product
from lfs.core.translation_utils import prepare_fields_order


class SEOForm(ModelForm):
    """Form to add/edit seo properties of a product.
    """
    def __init__(self, *args, **kwargs):
        super(SEOForm, self).__init__(*args, **kwargs)
        prepare_fields_order(self, fields=("active_meta_title", "meta_title",
                                           "active_meta_keywords", "meta_keywords",
                                           "active_meta_description", "meta_description",
                                           ))

    class Meta:
        model = Product
        fields = (
            "active_meta_title", "meta_title",
            "active_meta_keywords", "meta_keywords",
            "active_meta_description", "meta_description",
        )