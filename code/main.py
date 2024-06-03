import click
import os
import logging

from code.weather_reader import read_weather_data
from code.db_and_model import db
from code.flask_app import app
from code.utils import file_names_in_directory, commit_in_chunks

COMMIT_SIZE = 8192
logging.basicConfig(level=logging.DEBUG)


@click.group()
def cli():
    pass


@cli.command()
@click.argument('path', type=click.Path(exists=True, file_okay=False))
def read_data(path):
    with app.app_context():
        db.create_all()
        for file_name in file_names_in_directory(path):
            full_path = os.path.join(path, file_name)
            logging.debug(f"starting to read {full_path}")
            commit_in_chunks(db.session, read_weather_data(full_path), COMMIT_SIZE)
            logging.debug(f"finished to read {full_path}")


@cli.command()
def run():
    app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    cli()
