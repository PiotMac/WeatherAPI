import json
from weather_api import OpenMeteoProvider
from weather_logic import WeatherCategorizer

weather_provider = OpenMeteoProvider()
categorizer = WeatherCategorizer()

def lambda_handler(event, context):
    try:
        current_temperature = weather_provider.fetch_temperature()
        processed_temp = categorizer.process_temperature(current_temperature)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json; charset=utf-8"
            },
            "body": json.dumps(processed_temp)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"ERROR": str(e)})
        }