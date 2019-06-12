from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?:latlong=(?P<latitude>\d+\.\d{6})\,(?P<longitude>\d+\.\d{6}))?$', views.getlatitude)
]
