from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Float, String, Integer, DateTime, Index, UniqueConstraint
import os
from code.app import app

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
db = SQLAlchemy(app)


class WeatherData(db.Model):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    forecast_time = Column(DateTime, nullable=False)
    temperature = Column(Float, nullable=False)
    precipitation = Column(Float, nullable=False)

    __table_args__ = (
        Index('ix_longitude_latitude', 'longitude', 'latitude'),
        UniqueConstraint('longitude', 'latitude', 'forecast_time', name='uq_long_lat_time')
    )