from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.geos import GEOSGeometry
from .models import Userloclayer
from django.http import JsonResponse
from shapely.geometry import MultiPolygon, mapping, Point, Polygon, shape
from shapely.geometry.polygon import Polygon
import fiona
import json

# Create your views here.

def index(request):
    return HttpResponse("IIRS Survey App")

def getlocation(request, latitude, longitude, layer):
    point = {
        "type": "Point",
        "coordinates": [float(longitude), float(latitude)]
    }
    loclayer = Userloclayer.objects.create(location = GEOSGeometry(json.dumps(point)), layer = layer)
    loclayer.save()
    if layer == "Population":

        shphandle = ([ward for ward in fiona.open(r"C:\Users\abhis\Documents\IIRS Internship\Jupyter Lab\DDN_Geo.shp")])
        for index, ward in enumerate(shphandle):
        #    location = Point(float(longitude), float(latitude))
        #    if location.within(shape(ward['geometry'])):
        #        populationresponse = {
        #            "Ward No": ward['properties']['NUMBER1'],
        #            "Area Type": ward['properties']['TRU'],
        #            "Total People": ward['properties']['TOT_P'],
        #            "Total Males": ward['properties']['TOT_M'],
        #            "Total Females": ward['properties']['TOT_F'],
        #            "Total Literate People": ward['properties']['P_LIT'],
        #            "Total Literate Males": ward['properties']['M_LIT'],
        #            "Total Literate Females": ward['properties']['F_LIT'],
        #            "Total Illiterate People": ward['properties']['P_ILL'],
        #            "Total Illiterate Males": ward['properties']['M_ILL'],
        #            "Total Illiterate Females": ward['properties']['F_ILL'],
        #            "Total Working People": ward['properties']['TOT_WORK_P'],
        #            "Total Working Males": ward['properties']['TOT_WORK_M'],
        #            "Total Working Females": ward['properties']['TOT_WORK_F'],
        #            "Total Non Working People": ward['properties']['NON_WORK_P'],
        #            "Total Non Working Males": ward['properties']['NON_WORK_M'],
        #            "Total Non Working Females": ward['properties']['TOT_WORK_F']
        #        }
        #        return JsonResponse(populationresponse)
        #return HttpResponse("Location not inside any Ward")

            populationresponse = {
                "Ward No": ward['properties']['NUMBER1'],
                "Area Type": ward['properties']['TRU'],
                "Total People": ward['properties']['TOT_P'],
                "Total Males": ward['properties']['TOT_M'],
                "Total Females": ward['properties']['TOT_F'],
                "Total Literate People": ward['properties']['P_LIT'],
                "Total Literate Males": ward['properties']['M_LIT'],
                "Total Literate Females": ward['properties']['F_LIT'],
                "Total Illiterate People": ward['properties']['P_ILL'],
                "Total Illiterate Males": ward['properties']['M_ILL'],
                "Total Illiterate Females": ward['properties']['F_ILL'],
                "Total Working People": ward['properties']['TOT_WORK_P'],
                "Total Working Males": ward['properties']['TOT_WORK_M'],
                "Total Working Females": ward['properties']['TOT_WORK_F'],
                "Total Non Working People": ward['properties']['NON_WORK_P'],
                "Total Non Working Males": ward['properties']['NON_WORK_M'],
                "Total Non Working Females": ward['properties']['TOT_WORK_F']
            }
            return JsonResponse(populationresponse)


    if layer == "Soil":
        shphandle = ([ward for ward in fiona.open(r"C:\Users\abhis\Documents\IIRS Internship\Jupyter Lab\DDN_Geo.shp")])
        for index, ward in enumerate(shphandle):
            location = Point(float(longitude), float(latitude))
            if location.within(shape(ward['geometry'])):
                soilresponse = {
                    "Ward No": ward['properties']['NUMBER1']
                }
                return JsonResponse(soilresponse)
        return HttpResponse("Location not inside any Ward")

    if layer == "Drainage":
        shphandle = ([ward for ward in fiona.open(r"C:\Users\abhis\Documents\IIRS Internship\Jupyter Lab\DDN_Geo.shp")])
        for index, ward in enumerate(shphandle):
            location = Point(float(longitude), float(latitude))
            if location.within(shape(ward['geometry'])):
                drainageresponse = {
                    "Ward No": ward['properties']['NUMBER1']
                }
                return JsonResponse(drainageresponse)
        return HttpResponse("Location not inside any Ward")

    if layer == "Lithology":
        shphandle = ([ward for ward in fiona.open(r"C:\Users\abhis\Documents\IIRS Internship\Jupyter Lab\DDN_Geo.shp")])
        for index, ward in enumerate(shphandle):
            location = Point(float(longitude), float(latitude))
            if location.within(shape(ward['geometry'])):
                lithologyresponse = {
                    "Ward No": ward['properties']['NUMBER1']
                }
                return JsonResponse(lithologyresponse)
        return HttpResponse("Location not inside any Ward")

    if layer == "Geomorphology":
        shphandle = ([ward for ward in fiona.open(r"C:\Users\abhis\Documents\IIRS Internship\Jupyter Lab\DDN_Geo.shp")])
        for index, ward in enumerate(shphandle):
            location = Point(float(longitude), float(latitude))
            if location.within(shape(ward['geometry'])):
                geomorphoresponse = {
                    "Ward No": ward['properties']['NUMBER1']
                }
                return JsonResponse(geomorphoresponse)
        return HttpResponse("Location not inside any Ward")

    if layer == "Slope":
        shphandle = ([ward for ward in fiona.open(r"C:\Users\abhis\Documents\IIRS Internship\Jupyter Lab\DDN_Geo.shp")])
        for index, ward in enumerate(shphandle):
            location = Point(float(longitude), float(latitude))
            if location.within(shape(ward['geometry'])):
                sloperesponse = {
                    "Ward No": ward['properties']['NUMBER1']
                }
                return JsonResponse(sloperesponse)
        return HttpResponse("Location not inside any Ward")

    if layer == "Aspect":
        shphandle = ([ward for ward in fiona.open(r"C:\Users\abhis\Documents\IIRS Internship\Jupyter Lab\DDN_Geo.shp")])
        for index, ward in enumerate(shphandle):
            location = Point(float(longitude), float(latitude))
            if location.within(shape(ward['geometry'])):
                sloperesponse = {
                    "Ward No": ward['properties']['NUMBER1']
                }
                return JsonResponse(sloperesponse)
        return HttpResponse("Location not inside any Ward")
