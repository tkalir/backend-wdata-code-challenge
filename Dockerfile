FROM python:3.9-slim

WORKDIR /usr/app

COPY . .

RUN apt-get update && apt-get install -y postgresql-client

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["./build_scripts/entrypoint.sh"]

CMD ["python", "./code/main.py", "run"]