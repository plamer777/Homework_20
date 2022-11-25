"""The unit contains CBVs to work with /movies/ route"""
from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service
# -------------------------------------------------------------------------
movie_ns = Namespace('movies')
# -------------------------------------------------------------------------


@movie_ns.route('/')
class MoviesView(Resource):
    """The MoviesView class is CBV to work with /movies/ route"""
    def get(self) -> tuple:
        """This method processes GET requests

        :returns: a tuple containing a list of records and a status code
        """
        movies = movie_service.get_all()
        return MovieSchema(many=True).dump(movies), 200

    def post(self) -> tuple:
        """This method processes POST requests

        :returns: a tuple containing a result of the operation
        """
        req_json = request.json
        ent = movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{ent.id}"}


@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    """The MoviesView class is CBV to work with routes like /movies/1"""
    def get(self, bid) -> tuple:
        """The method processes GET requests

        :param bid: the id of searching record

        :returns: a tuple containing a dictionary and a status code
        """
        movie = movie_service.get_one(bid)
        return MovieSchema(many=True).dump(movie), 200

    def put(self, bid) -> tuple:
        """The method processes PUT requests

        :param bid: the id of searching record

        :returns: a tuple containing a result of the operation
        """
        req_json = request.json
        req_json["id"] = bid
        movie_service.update(req_json)
        return "", 204

    def patch(self, bid) -> tuple:
        """The method processes PATCH requests

        :param bid: the id of searching record

        :returns: a tuple containing a result of the operation
        """
        req_json = request.json
        req_json["id"] = bid
        movie_service.partially_update(req_json)
        return "", 204

    def delete(self, bid) -> tuple:
        """The method processes DELETE requests

        :param bid: the id of searching record

        :returns: a tuple containing a result of the operation
        """
        movie_service.delete(bid)
        return "", 204
