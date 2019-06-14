from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.geos import GEOSGeometry
from .models import Userloclayer
import fiona
from shapely.geometry import MultiPolygon, mapping, Point, Polygon, shape
from shapely.geometry.polygon import Polygon

# Create your views here.

def index(request):
    return HttpResponse("IIRS Survey App")

def getlocation(request, latitude, longitude, layer):
    shphandle = ([ward for ward in fiona.open(r"C:\Users\abhis\Documents\IIRS Internship\Jupyter Lab\DDN_Geo.shp")])
    point = {
        "type": "Point",
        "coordinates": [float(longitude), float(latitude)]
    }
    loclayer = Userloclayer.objects.create(location = GEOSGeometry(json.dumps(point)), layer = layer)
    loclayer.save()
    for index, ward in enumerate(shphandle):
        location = Point(float(longitude), float(latitude))
        if location.within(shape(ward['geometry'])):
            return HttpResponse(ward['properties']['Name'])
    return HttpResponse("Location not inside any Ward")
