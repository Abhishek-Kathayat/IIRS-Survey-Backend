from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?:@latlong=(?P<latitude>-?\d+\.\d{1,6})\,(?P<longitude>-?\d+\.\d{1,6}))?$', views.getlocation),
    path('layers', views.getLayers, name='layers')
]
