# django imports
from django.contrib import admin

# lfs imports
from lfs.customer.models import Customer, PreferredLanguage


class CustomerAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(Customer, CustomerAdmin)

admin.site.register(PreferredLanguage)