from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?:layer=(?P<layer>[\w]+))?(?:&latlong=(?P<latitude>-?\d+\.\d{5,6})\,(?P<longitude>-?\d+\.\d{5,6}))?$', views.getlocation)
]
