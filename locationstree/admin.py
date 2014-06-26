from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import Location


class LocationAdmin(MPTTModelAdmin):

    list_filter = ('level', )
    list_display = ('name', 'sort_order')
    list_editable = ('sort_order', )


admin.site.register(Location, LocationAdmin)
