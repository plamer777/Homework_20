"""The unit contains the Genre and GenreSchema classes to work with movie
table"""
from marshmallow import Schema, fields

from setup_db import db
# ------------------------------------------------------------------------


class Genre(db.Model):
    """The Genre class represents a model to work with genre table"""
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    """The GenreSchema class represents serializer/deserializer for Genre
    class models"""
    id = fields.Int()
    name = fields.Str()
