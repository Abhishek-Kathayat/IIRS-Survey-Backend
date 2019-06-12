from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def getlocation(request, latitude, longitude):
    location = {
        'latitude' : latitude,
        'longitude' : longitude
    }
    return JsonResponse(location)
