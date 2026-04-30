class WeatherCategorizer:
    def _categorize(self, temperature: float) -> str:
        if temperature < 0.0:
            return "Freezing"
        elif temperature < 10.0:
            return "Cold"
        elif temperature < 20.0:
            return "Mild"
        elif temperature < 25.0:
            return "Warm"
        else:
            return "Hot"

    def process_temperature(self, temperature: float) -> dict:
        return {
            "temperature": temperature,
            "category": self._categorize(temperature)
        }