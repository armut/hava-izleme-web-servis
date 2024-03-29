from django.contrib import admin
from django.urls import path, include
from kirli.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/kirli/', get_station_report, name='station_report'),
    path(r'api/kirli/istasyon_listesi', get_station_list, name='station_list'),
]
