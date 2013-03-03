# django imports
from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

# lfs imports
from lfs.core.models import Action
from lfs.core.models import ActionGroup
from lfs.core.models import Shop
from lfs.core.models import Country


class ActionGroupAdmin(TranslationAdmin):
    pass

class CountryAdmin(TranslationAdmin):
    pass

admin.site.register(Country, CountryAdmin)
admin.site.register(ActionGroup, ActionGroupAdmin)

admin.site.register(Shop)
admin.site.register(Action)

