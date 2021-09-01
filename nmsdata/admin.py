from django.contrib import admin

from .models import Device, Cell, Trx
# Register your models here.

admin.site.register(Device)
admin.site.register(Cell)
admin.site.register(Trx)