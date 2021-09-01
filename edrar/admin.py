from django.contrib import admin

from .models import Activity, SiteStatus, DailyActivity, MobileTechnology, MobileFrequencyBand
# Register your models here.

admin.site.register(Activity)
admin.site.register(SiteStatus)
admin.site.register(MobileTechnology)
admin.site.register(MobileFrequencyBand)
admin.site.register(DailyActivity)