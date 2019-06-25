from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Userloclayer, Layer


admin.site.register(Userloclayer)
admin.site.register(Layer)
