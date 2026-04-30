import json
from weather_api import OpenMeteoProvider
from weather_logic import WeatherCategorizer

weather_provider = OpenMeteoProvider()
categorizer = WeatherCategorizer()


def lambda_handler(event, context):
    try:
        city = None

        if 'city' in event:
            city = event['city']

        if not city:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "No parameter 'city' found. Provide city name."})
            }

        resolved_city, current_temp = weather_provider.get_weather(city)
        business_result = categorizer.format_response(resolved_city, current_temp)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json; charset=utf-8"
            },
            "body": json.dumps(business_result)
        }

    except ValueError as ve:
        # No provided city has been found
        return {
            "statusCode": 404,
            "body": json.dumps({"ERROR": str(ve)})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({f"ERROR: {str(e)}"})
        }