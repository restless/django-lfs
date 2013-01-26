# django imports
from django.forms import ModelForm

# lfs imports
from lfs.core.models import Action
from lfs.core.translation_utils import prepare_fields_order

class ActionForm(ModelForm):
    """Form to edit an action.
    """
    def __init__(self, *args, **kwargs):
        super(ActionForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = prepare_fields_order(self, 'active', 'title', 'link', 'group')

    class Meta:
        model = Action


class ActionAddForm(ModelForm):
    """Form to add a action
    """
    def __init__(self, *args, **kwargs):
        super(ActionAddForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = prepare_fields_order(self, "title", "link", "group")

    class Meta:
        model = Action
