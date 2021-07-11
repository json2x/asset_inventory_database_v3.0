from django.contrib import admin
#from .models import ApiUserToken, Cell, Device, Location, SiteNeAsset, SmartNe, SmartSite, TocAor
from .models import Cell, Device, Location, SiteNeAsset, SmartNe, SmartSite, TocAor
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from django.utils.html import format_html
'''
class ApiUserTokenInline(admin.StackedInline):
    model = ApiUserToken
    fk_name = 'user'
    extra = 1
    max_num = 1
    fields = ['access_token', 'refresh_token', 'generate_button']
    readonly_fields = ('generate_button',)

    class Media:
        css = {
            'all': ('api/css/adminCustomDOM.css',)
        }
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',
            'api/js/genApiKeys.js',
        )
    
    def generate_button(self, obj):
        return format_html("<button class='admin-custom-btn' id='generateKey' type='button'>Generate Keys</button>")

class CustomUserAdmin(UserAdmin):
    inlines = [ApiUserTokenInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
'''
admin.site.register(SmartSite)
admin.site.register(SmartNe)
admin.site.register(Device)
admin.site.register(Cell)
admin.site.register(SiteNeAsset)

admin.site.register(Location)
admin.site.register(TocAor)



# Register your models here.
