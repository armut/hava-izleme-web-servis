from django.shortcuts import render
from django.http import JsonResponse
import tools
import json
from time import sleep

def get_station_report(request):
    if request.method == 'GET':
        if 'istasyon' in request.GET and 'tarih' in request.GET:
            if request.GET.get('istasyon') == 'hepsi':
                result = {}
                for station in tools.station_dict.keys():
                    try:
                        result[station] = tools.parser(station, request.GET.get('tarih'))
                    except requests.exceptions.ConnectionError:
                        return JsonResponse({'Hata': 'Sunucu cevap vermeyi reddetti.'})
                return JsonResponse(result)
            else:
                try:
                    return JsonResponse(tools.parser(request.GET.get('istasyon'), request.GET.get('tarih')))
                except:
                    return JsonResponse({
                        'Hata': 'Hatayı açıklamayan hata mesajlarından ben de hiç hoşlanmıyorum ama hatanın sebebini gerçekten bilmiyorum.'
                    })
        
def get_station_list(request):
    if request.method == 'GET':
        return JsonResponse(tools.station_dict)
                
