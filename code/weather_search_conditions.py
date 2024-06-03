def very_hot_predicate(weather_data):
    return weather_data.temperature > 30


def rainy_and_cold_predicate(weather_data):
    return weather_data.temperature < 10 and weather_data.precipitation > 0.5


search_weather_conditions = {}
search_weather_conditions["veryHot"] = very_hot_predicate
search_weather_conditions["rainyAndCold"] = rainy_and_cold_predicate


def get_condition_object(condition_string):
    return search_weather_conditions[condition_string]