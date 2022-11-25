"""This is a main file to start the Flask application"""
from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
# ------------------------------------------------------------------------


def create_app(config_object: Config) -> Flask:
    """The function creates configured application with all extensions

    :param config_object: the class with necessary settings

    :returns: an instance of the Flask
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app: Flask) -> None:
    """The function configure extensions such as database and Api instances

    :param app: an instance of Flask with required settings
    """
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    create_data(app, db)


def create_data(app: Flask, db) -> None:
    """The function creates database tables

    :param app: an instance of Flask
    :param db: an instance of SQLAlchemy
    """
    with app.app_context():
        db.create_all()
# ------------------------------------------------------------------------


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
