"""This unit contains configuration classes and another objects to configure
the application"""


class Config(object):
    """The Config class with necessary settings"""
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

