from django.contrib import admin
from .models import Cell, Device, Location, SiteNeAsset, SmartNe, SmartSite, TocAor
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from django.utils.html import format_html

admin.site.register(SmartSite)
admin.site.register(SmartNe)
admin.site.register(Device)
admin.site.register(Cell)
admin.site.register(SiteNeAsset)

admin.site.register(Location)
admin.site.register(TocAor)



# Register your models here.
