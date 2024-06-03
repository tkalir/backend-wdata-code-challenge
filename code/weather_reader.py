import csv
from datetime import datetime

from db_and_model import WeatherData

LATITUDE_CSV_COL = 'Latitude'
LONGITUDE_CSV_COL = 'Longitude'
FORCAST_TIME_CSV_COL = 'forecast_time'
TEMPERATURE_CSV_COL = 'Temperature Celsius'
PRECIPITATION_CSV_COL_PREFIX = "precipitation rate"

INCH_TO_MM_RATION = 25.4


# fieldnames - column headers in the csv file
# returns header that is related to precipitation & ratio of its units to mm
def parse_precipitation_header(fieldnames):
    rates = {"mm/hr": 1, "in/hr": INCH_TO_MM_RATION}
    for fieldname in fieldnames:
        if fieldname.lower().startswith(PRECIPITATION_CSV_COL_PREFIX):
            words = fieldname.split(" ")
            rate = words[-1]
            return fieldname, rates[rate]


def read_weather_data(file_path: str):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        precipitation_header, precipitation_multiplier = parse_precipitation_header(csv_reader.fieldnames)

        for row in csv_reader:
            try:
                weather_data = WeatherData(
                    longitude=float(row[LONGITUDE_CSV_COL]),
                    latitude=float(row[LATITUDE_CSV_COL]),
                    forecast_time=datetime.fromisoformat(row[FORCAST_TIME_CSV_COL]),
                    temperature=float(row[TEMPERATURE_CSV_COL]),
                    precipitation=float(row[precipitation_header]) * precipitation_multiplier
                )
                yield weather_data
            except ValueError as e:
                raise ValueError(f"Invalid data format in row: {row}. Error: {e}")
