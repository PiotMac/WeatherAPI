class WeatherCategorizer:
    def categorize(self, temperature: float) -> str:
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

    def format_response(self, city_name: str, temperature: float) -> dict:
        return {
            "location": city_name,
            "temperature": temperature,
            "category": self.categorize(temperature)
        }