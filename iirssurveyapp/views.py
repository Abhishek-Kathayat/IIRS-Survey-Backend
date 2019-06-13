from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.gis.geos import GEOSGeometry
from .models import Userloclayer

import json

# Create your views here.

def index(request):
    return HttpResponse("IIRS Survey App")

def getlocation(request, latitude, longitude, layer):
    point = {
        "type": "Point",
        "coordinates": [float(latitude), float(longitude)]
    }
    loclayer = Userloclayer.objects.create(location = GEOSGeometry(json.dumps(point)), layer = layer)
    loclayer.save()
    return HttpResponse("Values Inserted")
