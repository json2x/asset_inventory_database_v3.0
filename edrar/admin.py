from django.contrib import admin

from .models import Activity, SiteStatus, DailyActivity, MobileTechnology, MobileFrequencyBand
from .models import DailyActivity_Device, DailyActivity_Cell, DailyActivity_Trx
# Register your models here.

admin.site.register(Activity)
admin.site.register(SiteStatus)
admin.site.register(MobileTechnology)
admin.site.register(MobileFrequencyBand)

class DailyActivity_Admin(admin.ModelAdmin):
    list_display = ('id', 'date_logged', 'activity', 'siteid', 'tech', 'band', 'vendor')
admin.site.register(DailyActivity, DailyActivity_Admin)

class DailyActivity_Device_Admin(admin.ModelAdmin):
    list_display = ('id', 'date', 'daily_activity', 'device', 'create_flag', 'update_flag')
admin.site.register(DailyActivity_Device, DailyActivity_Device_Admin)

class DailyActivity_Cell_Admin(admin.ModelAdmin):
    list_display = ('id', 'date', 'daily_activity', 'cell', 'create_flag', 'update_flag')
admin.site.register(DailyActivity_Cell, DailyActivity_Cell_Admin)

class DailyActivity_Trx_Admin(admin.ModelAdmin):
    list_display = ('id', 'date', 'daily_activity', 'trx', 'create_flag', 'update_flag')
admin.site.register(DailyActivity_Trx, DailyActivity_Trx_Admin)