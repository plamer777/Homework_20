"""The unit contains CBVs to work with /genres/ route"""
from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service
# -------------------------------------------------------------------------
genre_ns = Namespace('genres')
# -------------------------------------------------------------------------


@genre_ns.route('/')
class GenresView(Resource):
    """The GenresView class is CBV to work with /genres/ route"""
    def get(self) -> tuple:
        """This method processes GET requests

        :returns: a tuple containing a list of records and a status code
        """
        genres = genre_service.get_all()
        return GenreSchema(many=True).dump(genres), 200

    def post(self) -> tuple:
        """This method processes POST requests

        :returns: a tuple containing a result of the operation
        """
        req_json = request.json
        ent = genre_service.create(req_json)
        return "", 201, {"location": f"/genres/{ent.id}"}


@genre_ns.route('/<int:bid>')
class GenreView(Resource):
    """The GenresView class is CBV to work with routes like /genres/1"""
    def get(self, bid) -> tuple:
        """The method processes GET requests

        :param bid: the id of searching record

        :returns: a tuple containing a dictionary and a status code
        """
        genre = genre_service.get_one(bid)
        return GenreSchema().dump(genre), 200

    def put(self, bid) -> tuple:
        """The method processes PUT requests

        :param bid: the id of searching record

        :returns: a tuple containing a result of the operation
        """
        req_json = request.json
        req_json["id"] = bid
        genre_service.update(req_json)
        return "", 204

    def patch(self, bid) -> tuple:
        """The method processes PATCH requests

        :param bid: the id of searching record

        :returns: a tuple containing a result of the operation
        """
        req_json = request.json
        req_json["id"] = bid
        genre_service.partially_update(req_json)
        return "", 204

    def delete(self, bid) -> tuple:
        """The method processes DELETE requests

        :param bid: the id of searching record

        :returns: a tuple containing a result of the operation
        """
        genre_service.delete(bid)
        return "", 204
