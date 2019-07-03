from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.geos import GEOSGeometry
from .models import Userloclayer, Layer
from django.http import JsonResponse
from shapely.geometry import MultiPolygon, mapping, Point, Polygon, shape
from shapely.geometry.polygon import Polygon
from django.core import serializers
import fiona
import json
import os
import fnmatch
import geopandas


def index(request):
    return HttpResponse("IIRS Survey App")

def getLayers(request):
    layers = Layer.objects.all()
    layerresponse = [
        {
            'layer': str(layer)
        }
        for layer in list(layers)
    ]
    return JsonResponse(layerresponse, safe=False)

def getlocation(request, latitude, longitude):
    point = {
        "type": "Point",
        "coordinates": [float(longitude), float(latitude)]
    }
    loclayer = Userloclayer.objects.create(location = GEOSGeometry(json.dumps(point)))
    loclayer.save()

    shapefiles = list()
    for file_name in os.listdir('C:/Users/abhis/Documents/IIRS Internship/Jupyter Lab/ShapeFiles/Modified ShapeFiles/'):
        if fnmatch.fnmatch(file_name, '*.shp'):
            shapefiles.append(file_name)

    for shapefile in shapefiles:
        filehandle = geopandas.read_file('C:/Users/abhis/Documents/IIRS Internship/Jupyter Lab/ShapeFiles/Modified ShapeFiles/' + shapefile)
        file_crs = filehandle.crs
        if(file_crs['init'] != 'epsg:4326'):
            filehandle = filehandle.to_crs({'init': 'epsg:4326'})
            filehandle.to_file('C:/Users/abhis/Documents/IIRS Internship/Jupyter Lab/ShapeFiles/Modified ShapeFiles/Temp_data.shp')
        else:
            filehandle.to_file('C:/Users/abhis/Documents/IIRS Internship/Jupyter Lab/ShapeFiles/Modified ShapeFiles/Temp_data.shp')

        shphandle = ([ward for ward in fiona.open(r"C:\Users\abhis\Documents\IIRS Internship\Jupyter Lab\ShapeFiles\Modified ShapeFiles\Temp_data.shp")])
        for index, ward in enumerate(shphandle):
            location = Point(float(longitude), float(latitude))
            #if location.within(shape(ward['geometry'])):
            if shapefile == 'Drainage.shp':
                drainage = {
                }
            elif shapefile == 'DDN_Geo.shp':
                population = {
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
            elif shapefile == 'Geomorphology.shp':
                geomorphology = {
                    "Area": ward['properties']['AREA'],
                    "Geomorphology Class": ward['properties']['GEOM_CLASS'],
                    "Perimeter": ward['properties']['PERIMETER'],
                    "Regional_1": ward['properties']['REGIONAL_1'],
                    "Regional_G": ward['properties']['REGIONAL_G'],
                    "Geomorphology Score": ward['properties']['geo_score']
                }
            elif shapefile == 'Lithology.shp':
                lithology = {
                    "Geology": ward['properties']['GEOLOGY_'],
                    "Geology ID": ward['properties']['GEOLOGY_ID'],
                    "Area": ward['properties']['Shape_Area'],
                    "Lithology": ward['properties']['LITHOLOGY'],
                    "Perimeter": ward['properties']['PERIMETER'],
                    "Lithology Score": ward['properties']['lit_score']
                }
            elif shapefile == 'Existing_Site.shp':
                existing_site = {
                }
            elif shapefile == 'Slope.shp':
                slope = {
                    "Grid Code": ward['properties']['grid_code'],
                    "Slope Degree": ward['properties']['slope_degr'],
                    "Slope Score": ward['properties']['slop_score'],
                    "Area": ward['properties']['Shape_Area']
                }
            elif shapefile == 'Soil.shp':
                soil = {
                    "Soil Code": ward['properties']['SO_CODE'],
                    "Soil Type": ward['properties']['SOIL_TYPE'],
                    "Soil Depth": ward['properties']['SoilDepth'],
                    "Soil Erosion": ward['properties']['SoilErosio'],
                    "Soil Texture": ward['properties']['SoilTextur'],
                    "Soil Score": ward['properties']['soil_score'],
                    "GeoTOPSYS": ward['properties']['geoTOPSYS']
                }
            elif shapefile == 'LULC_12Classes.shp':
                lulc_class = {
                    "Land Usage Score": ward['properties']['lu_score'],
                    "Land Usage Class": ward['properties']['lu_class'],
                    "Land Usage": ward['properties']['r1_lulc'],
                    "Area": ward['properties']['Shape_Area']
                }
            break

    responsedata = {}
    responsedata["Soil"] = soil
    responsedata["Geomorphology"] = geomorphology
    responsedata["Lithology"] = lithology
    responsedata["Population"] = population
    responsedata["Slope"] = slope
    responsedata["Land Usage"] = lulc_class

    return JsonResponse(responsedata)

            #elif shapefile in ['Hospitals.shp', 'Institutions.shp', 'MajorCityPoints.shp', 'OSM_Infra.shp', 'OSM_Points.shp']:
            #    loc_file = ward['geometry']
            #    wardhandle = ([wardloc for wardloc in fiona.open(r"C:\Users\abhis\Documents\IIRS Internship\Jupyter Lab\ShapeFiles\Modified ShapeFiles\DDN_Geo.shp")])
            #    for index, wardloc in enumerate(wardhandle):
            #        if location.within(shape(wardloc['geometry'])) and loc_file.within(shape(wardloc['geometry'])):
            #            if shapefile is 'Hospital.shp':
            #                hospital = {
            #                    "FID_Hospital": ward['properties']['FID_HOSPIT'],
            #                    "Hospital Name": ward['properties']['NAME'],
            #                    "FID_Municipality": ward['properties']['FID_MUNICI'],
            #                    "Area Type": ward['properties']['TRU']
            #                }
            #                break
            #            elif shapefile is 'Institutions.shp':
            #                institutions = {
            #                    "FID_Institute": ward['properties']['FID_INSTIT'],
            #                    "Institute Name": ward['properties']['Name'],
            #                    "Nearby Place": ward['properties']['nearby_pla'],
            #                    "Area Type": ward['properties']['TRU'],
            #                    "FID_MUNICI": ward['properties']['FID_MUNICI']
            #                }
            #                break
            #            elif shapefile is 'MajorCityPoints.shp':
            #                majorcitypoints =  {
            #                    "ID": ward['properties']['Id'],
            #                    "Grid Code": ward['properties']['grid_code'],
            #                    "Original FID": ward['properties']['ORIG_FID']
            #                }
            #                break
            #            elif shapefile is 'OSM_Infra.shp':
            #                osm_infra = {
            #                    "Name": ward['properties']['ONGC Telbhawan'],
            #                    "Amenity": ward['properties']['public_building']
            #                }
            #                break
