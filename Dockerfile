FROM python:3.9-slim

WORKDIR /usr/app

COPY . .

RUN apt-get update && apt-get install -y postgresql-client

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

RUN chmod +x "./build_scripts/entrypoint.sh"
RUN chmod +x "./build_scripts/first_start.sh"
RUN chmod +x "./build_scripts/wait-for-db.sh"

ENTRYPOINT ["./build_scripts/entrypoint.sh"]

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "code.flask_app:app"]