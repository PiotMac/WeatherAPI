import json
import urllib.request
from abc import ABC, abstractmethod

class WeatherProvider(ABC):
    @abstractmethod
    def fetch_temperature(self) -> float:
        pass

class OpenMeteoProvider(WeatherProvider):
    def __init__(self):
        self.url = "https://api.open-meteo.com/v1/forecast?latitude=51.107883&longitude=17.0333&current=temperature_2m"

    def fetch_temperature(self) -> float:
        req = urllib.request.Request(self.url)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            return float(data['current']['temperature_2m'])