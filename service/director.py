"""The unit contains the DirectorService class providing a business logic to
interact with directors' data"""
from dao.director import DirectorDAO
# -----------------------------------------------------------------------


class DirectorService:
    """The DirectorService class with necessary business logic"""
    def __init__(self, dao: DirectorDAO) -> None:
        """The initialization of the DirectorService class

        :param dao: an instance of DirectorDAO class
        """
        self.dao = dao

    def get_one(self, bid):
        """The method returns a single record found in the database

        :param bid: the id of the searching record

        :returns: a model with dota of found record
        """
        return self.dao.get_one(bid)

    def get_all(self) -> list:
        """The method returns a list of records found in the database

        :returns: a list of models
        """
        return self.dao.get_all()

    def create(self, director_d):
        """The method creates a new record in the database

        :param director_d: a dictionary with data to create the record

        :returns: a model with dota of created record
        """
        return self.dao.create(director_d)

    def update(self, director_d) -> None:
        """The method updates a record in the database

        :param director_d: a dictionary with data to update
        """
        return self.dao.update(director_d)

    def partially_update(self, director_d) -> None:
        """The method partially updates a record in the database

        :param director_d: a dictionary with data to update
        """
        director = self.get_one(director_d["id"])
        if "name" in director_d:
            director.name = director_d.get("name")
        self.dao.update(director)

    def delete(self, rid) -> None:
        """The method deletes a record from the database

        :param rid: an id of the deleted record
        """
        self.dao.delete(rid)
