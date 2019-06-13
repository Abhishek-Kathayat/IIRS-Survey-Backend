from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Userloclayer
# Register your models here.

@admin.register(Userloclayer)
class UserloclayerAdmin(OSMGeoAdmin):
    list_display = ('location', 'layer')
