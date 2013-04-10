from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import Location


admin.site.register(Location, MPTTModelAdmin)
