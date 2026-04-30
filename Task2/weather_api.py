import urllib.request
import urllib.parse
import json
from abc import ABC, abstractmethod


class WeatherProvider(ABC):
    @abstractmethod
    def get_weather(self, city_name: str) -> tuple[str, float]:
        """Returns a tuple: (City name, Temperature)"""
        pass


class OpenMeteoProvider(WeatherProvider):
    def __init__(self):
        self.geocode_url = "https://geocoding-api.open-meteo.com/v1/search?name={}&count=1&language=en&format=json"
        self.weather_url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current=temperature_2m"

    def _get_coordinates(self, city_name: str) -> tuple[float, float, str]:
        safe_city = urllib.parse.quote(city_name)
        req = urllib.request.Request(self.geocode_url.format(safe_city))
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            if not data.get('results'):
                raise ValueError(f"Couldn't find city: '{city_name}'")
            location = data['results'][0]
            return location['latitude'], location['longitude'], location['name']

    def get_weather(self, city_name: str) -> tuple[str, float]:
        lat, lon, resolved_city = self._get_coordinates(city_name)

        req = urllib.request.Request(self.weather_url.format(lat, lon))
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            temperature = float(data['current']['temperature_2m'])

        return resolved_city, temperature
