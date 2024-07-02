from django.urls import path
from . import views

urlpatterns = [
    path('weather/<str:city_name>/', views.get_weather, name='get_weather'),
    # path('aqi/<str:city_name>/', views.get_aqi, name='get_aqi'),
    # path('aqi/<slug:lat>/<slug:lon>/', views.get_aqi, name='get_aqi'),
    # path('aqi/<decimal:lat>/<decimal:lon>/', views.get_aqi, name='get_aqi'),  
     path('aqi/(?P<lat>-?\d+\.\d+)/(?P<lon>-?\d+\.\d+)/', views.get_aqi, name='get_aqi'),
]
