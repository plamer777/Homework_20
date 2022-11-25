"""The unit contains CBVs to work with /directors/ route"""
from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service
# -------------------------------------------------------------------------
director_ns = Namespace('directors')
# -------------------------------------------------------------------------


@director_ns.route('/')
class DirectorsView(Resource):
    """The DirectorsView class is CBV to work with /directors/ route"""
    def get(self) -> tuple:
        """This method processes GET requests

        :returns: a tuple containing a list of records and a status code
        """
        directors = director_service.get_all()
        return DirectorSchema(many=True).dump(directors), 200

    def post(self) -> tuple:
        """This method processes POST requests

        :returns: a tuple containing a result of the operation
        """
        req_json = request.json
        ent = director_service.create(req_json)
        return "", 201, {"location": f"/directors/{ent.id}"}


@director_ns.route('/<int:bid>')
class DirectorView(Resource):
    """The DirectorView class is CBV to work with routes like /directors/1"""
    def get(self, bid) -> tuple:
        """The method processes GET requests

        :param bid: the id of searching record

        :returns: a tuple containing a dictionary and a status code
        """
        director = director_service.get_one(bid)
        return DirectorSchema().dump(director), 200

    def put(self, bid) -> tuple:
        """The method processes PUT requests

        :param bid: the id of searching record

        :returns: a tuple containing a result of the operation
        """
        req_json = request.json
        req_json["id"] = bid
        director_service.update(req_json)
        return "", 204

    def patch(self, bid) -> tuple:
        """The method processes PATCH requests

        :param bid: the id of searching record

        :returns: a tuple containing a result of the operation
        """
        req_json = request.json
        req_json["id"] = bid
        director_service.partially_update(req_json)
        return "", 204

    def delete(self, bid) -> tuple:
        """The method processes DELETE requests

        :param bid: the id of searching record

        :returns: a tuple containing a result of the operation
        """
        director_service.delete(bid)
        return "", 204
