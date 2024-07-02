# api/views.py

from django.http import HttpResponse, JsonResponse
import requests
import json

def get_weather(request, city_name):
    api_key = '6708c911f34cb3cf4a52441630605667'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if data.get('cod') == 200:
        weather_data = {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'description': data['weather'][0]['description']
        }
        return JsonResponse(weather_data)
    else:
        return JsonResponse({'error': 'Weather data not found'}, status=404)

def get_aqi(request, lat, lon):
    api_key = '6708c911f34cb3cf4a52441630605667'
    aqi_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"

    response = requests.get(aqi_url)
    if response.status_code == 200:
        aqi_data = response.json()
        return HttpResponse(json.dumps(aqi_data), content_type='application/json')
    else:
        return HttpResponse(json.dumps({"error": "Air quality data not found"}), status=response.status_code, content_type='application/json')
