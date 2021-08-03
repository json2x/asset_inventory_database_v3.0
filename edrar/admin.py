from django.contrib import admin

from .models import Activity, SiteStatus, DailyActivity
# Register your models here.

admin.site.register(Activity)
admin.site.register(SiteStatus)
admin.site.register(DailyActivity)