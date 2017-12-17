from django.contrib import admin
from django.urls import path, include
from kirli.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/', get_station_report, name='station_report')
]
