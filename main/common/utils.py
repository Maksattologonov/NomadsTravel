import requests

from django.conf import settings
from datetime import datetime
from django.conf import settings


def time_of_function(function):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        res = function()
        print(datetime.now() - start)
        return res
    return wrapper

def get_weather(lat, lon):
    api_key = settings.OPENWEATHER_API_KEY  # Добавь ключ в settings.py
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={settings.OPEN_WEATHER_MAP_TOKEN}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def avg(arr: list) -> float:
    return sum(arr) / len(arr)


def get_elevation(lat, lon):
    url = f'https://api.open-elevation.com/api/v1/lookup?locations={lat},{lon}'
    response = requests.get(url)
    if response.status_code == 200:
        print(response.content)
        return response.json()['results'][0]['elevation']

