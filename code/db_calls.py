from code.db_and_model import WeatherData, db
from sqlalchemy import and_


def search_weather(lat, lon):
    query = db.session.query(WeatherData).filter(
        and_(
            WeatherData.longitude == lon,
            WeatherData.latitude == lat
        )
    ).order_by(WeatherData.forecast_time)

    return query.all()