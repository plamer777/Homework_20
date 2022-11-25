"""The unit contains the Director and DirectorSchema classes to work with
director table"""
from setup_db import db
from marshmallow import Schema, fields


class Director(db.Model):
    """The Director class represents a model to work with director table"""
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    """The DirectorSchema class represents serializer/deserializer for Director
    class models"""
    id = fields.Int()
    name = fields.Str()
