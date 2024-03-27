# backend-wdata-code-challenge - Weather Data Team Candidate Home Work

## Abstract
Let's build a weather service. In this task, you will digest the weather data source and expose it via an amazing API that you are going to build!

### CSV Files
For this task, we will use CSV files as our data source just to make it simple. In the "real world", we won't use CSV, but other formats that are more optimized for weather data such as NetCDF, Zarr. Attached you will find 3 files in CSV format. The files represent weather forecast data. The files are world coverage so you will be able to know what is the weather all over the world! Each file represents a weather forecast of a different time (day/hour). 

**BTW**: this is just mock data, don't try to plan your next trip based on this forecast :)

## The Task
In this task, we want you to create a web service that will give us the weather forecast for a specific location. Each file has 5 columns: Longitude, Latitude, forecast time, Temperature, Precipitation. The service will have 2 routes:

1. `/weather/data` - returns the weather forecast in a specific location.
2. `/weather/summarize` - returns the max, min, avg weather data (from all the files) for a specific location.

Temperature in Celsius, Precipitation Rate in mm/hr.

### Service Explanation
#### Route: `/weather/data`
- **Query Parameters**: lat, lon
- **Output (JSON) - Example**:
    ```json
    [
      {
        "forecastTime": "2018-12-10T13:00:00.000Z",
        "Temperature": 23.3,
        "Precipitation": 32.1,
      },
      {
        "forecastTime": "2018-12-10T14:00:00.000Z",
        "Temperature": 33,
        "Precipitation": 12,
      },
      {
        "forecastTime": "2018-12-10T15:00:00.000Z",
        "Temperature": 13.1,
        "Precipitation": 15,
      },
    ]
    ```

#### Route: `/weather/summarize`
- **Query Parameters**: lat, lon
- **Output (JSON)**:
    ```json
    {
      "max": {
          "Temperature": 33,
          "Precipitation": 20,
      },
      "min": {
          "Temperature": 13,
          "Precipitation": 3,
      },
      "avg": {
          "Temperature": 20.45,
          "Precipitation": 12.4,
      }
    }
    ```

## What is Expected
- Send us a URL to a working service with an example of how to use it. For example: `http://my-cool-service.com/weather/data?lat=42.332&lon=35.421`
- Send us the source code, or even better, a link to a git repository with the source code.

### Implementation
The service should have 2 parts:
1. Ingest the CSV into Database.
2. Web Server that reads the data from the Database and displays it.

### Tips
- **Programming Language**: Pick whatever you like, pick the language that you are most comfortable with.
- **Database**: SQL/NoSQL, whatever you think will be fast and good for this task.
- You can use any free hosting provider such as render.com, Heroku, AWS, GCS, Azure, DigitalOcean, etc... (if you don't know any of them, we recommend using render.com as it is the easiest to start with and we tested that task can run on it).
- Take your time to go over the instructions and attached data before you begin.

### General
- Attach to your task a list of things that you think should be optimized/pitfalls in your solution.
- Write any assumptions that you make (if any).
- This is not a production service, but we will be happy to know what is missing to make it one.
- If you think that you are investing too much time on the task, please let us know and write what is missing to complete it.

### Data Source Links
- [File 1](https://storage.googleapis.com/tomorrow-external-access/Data-Team-Candidate-Home-Work-Task/File1.csv)
- [File 2](https://storage.googleapis.com/tomorrow-external-access/Data-Team-Candidate-Home-Work-Task/File2.csv)
- [File 3](https://storage.googleapis.com/tomorrow-external-access/Data-Team-Candidate-Home-Work-Task/File3.csv)


## Questions?
Please contact us, WhatsApp, email, phone call.

**Good luck!**
