from flask import Flask, request, jsonify
import logging

from code.db_calls import search_weather
from code.weather_search_conditions import get_condition_object
from code.app import app

WEATHER_INSIGHT_URL = "/weather/insight"


@app.route(WEATHER_INSIGHT_URL, methods=['GET'])
def weather_insight():
    try:
        condition_string = request.args.get('condition')
        lat = float(request.args.get('lat'))
        lon = float(request.args.get('lon'))
        condition_function = get_condition_object(condition_string)
    except Exception:
        return jsonify({"error": "Invalid parameters"}), 400

    try:
        results = [create_weather_insight(data, condition_function) for data in search_weather(lat, lon)]
        return jsonify(results)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", str(e), exc_info=True)
        return jsonify({"error": "An unexpected error occurred"}), 500


def create_weather_insight(weather_data, condition_function):
    return {"forecast_time": weather_data.forecast_time.isoformat() + "Z",
            "conditionMet": condition_function(weather_data)}