# django imports
from django.contrib import admin

# lfs imports
from lfs.core.models import Action
from lfs.core.models import ActionGroup
from lfs.core.models import Shop
from lfs.core.models import Country
from lfs.core.translation_utils import LFSTranslationAdmin


class ActionGroupAdmin(LFSTranslationAdmin):
    pass

class CountryAdmin(LFSTranslationAdmin):
    pass

admin.site.register(Country, CountryAdmin)
admin.site.register(ActionGroup, ActionGroupAdmin)

admin.site.register(Shop)
admin.site.register(Action)

