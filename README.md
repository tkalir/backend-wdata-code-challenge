# backend-wdata-code-challenge - Weather Data Team Candidate Home Work

# How to use this service

The following ip 35.157.192.227 is the public ip of my Amazon Lightsail instance, <br />
which runs docker-compose with two containers, a Flask server and a Postgres database.<br />

Example of usage:

``` 
curl "http://35.157.192.227:5000/weather/insight?lon=51.5&lat=24.5&condition=veryHot"
```

Running locally:

```
git clone https://github.com/tkalir/backend-wdata-code-challenge.git && docker compose up
```

The service is reachable through port 5000.

# Optimizations

* **Parallelism** - the input files are currently being read serially. given that there is no dependency in the data
  between the files,
  we can easily read and injest multiple files at the same time.

  One way to achieve that is by using a task queue like Celery. <br />
  Assuming we have all the data before starting the server,
  we can create a task for each file and start the workers. <br>
  Combined with a platform like Airflow we can see, re-run and get notified about failed tasks (i.e file arrived
  corrupted).
* **Caching** - Assuming some cordinates are more asked upon than others, it might be useful to use a cache like Redis
  to store results instead of querying the database every time.

# Improvements

* **Error handling** - if the db did not start regularly, we might want to not start the server at all.
  We might also want to alert a monitoring system like Sentry.
    * currently if the app has an error while reading a csv line, it stops reading the files. <br>
      In the real world we might create a queue of mishandled lines (or files) and have an easy api for <br>
      fixing the issue and re-injest them.
* **Input formats** - The app currently supports only csv files with the column headers that appear in the example files.   
  Support can be added for other formats, like files with header "Temperature Farenheit" or "lat" instead of "latitude".
* **Tests** - we can add automatic tests to make sure features do not break in the future. <br> Pytest for example has
  fixtures to simulate data in the database and tools (test_client) to test what happens upon request.
* **Deployment** - the app is currently deployed on Lightsail, running via docker compose on a virtual machine.<br>
  A more robust approach would be to run the containers using a managed service. <br>
* **Security** - The app does not have a certificate, so it can't use https, making it possible to impersonate the site.
  <br>
  The server is also vulnerable to DDOS attacks. To mitigate that in the current setting, if we had a domain, we could point it
  to a service like Cloudflare that filters out suspicous traffic and fordwards to our server only the legitimate one.
* **CI\CD** - we could create infrastructure to automatically run tests and deploy the code to our server, using github
  actions for example.
* **migration tool** - in the future we might want to change the database schema, so we could introduce a migration tool
  (like alembic) to our system in order the manage the schema changes.

# Production-readiness and scale

Handling the previous points would make the app more production-ready assuming we have relatively small traffic. <br>
Having lots of data to process, or many requests to handle, may require us to use a service like Kubernetes to have
multiple machines performing these tasks. Additionally we might want to separate the data-ingestion and the webapp parts
to different services, to be able to scale them independently.

# Remarks and considerations

* In my solution I opted to go for the simpler solution that solves the given task instead of trying to anticipate <br>
  future requirements. <br>
  For example, it makes sense that the user will be able to send conditions with parameters, like temp>10. <br>
  Instead of trying to anticipate how future conditions would look, I preferred to go for a simple solution and keep all
  the conditions-related code in one file and accessible by a single function (get_condition_object) so it will be easy
  to change the implementation for that module when future requirements arrive.
* I could implement the condition checks in two ways - check the condition inside the sql query and return the answer,
  or I could fetch the whole WeatherData object from the database and check the condition later. I chose the latter
  because it is more flexible in case future conditions are more complicated and can't be expressed in sql, and it
  creates a better divide between the app logic and the database logic. <br>
  It does mean we fetch unnecessary data from the database, so it's a tradeoff and optimization can be done in the
  future.
* Creating the server dockerfile I took into consideration that we want to read the data into the database only
  the first time the container starts, otherwise we will read the same data again, which will be wasted effort and cause
  unique-constraint errors in my implementation.
  Making the data ingestion part of the image build seems less debugable (and makes it a less useful image), so I used
  a script that uses an empty file ("first_start_complete") as a flag and the first time the container runs it
  triggers <br>
  the data ingestion and then creates the flag.
