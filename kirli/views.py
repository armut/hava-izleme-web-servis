from django.shortcuts import render
from django.http import JsonResponse
from tools import *
import json

def get_station_report(request):
    if request.method == 'GET':
        if 'station' in request.GET and 'date' in request.GET:
            return JsonResponse(parser(request.GET.get('station'), request.GET.get('date')))
