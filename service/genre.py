"""The unit contains the GenreService class providing a business logic to
interact with genres' data"""
from dao.genre import GenreDAO
# -----------------------------------------------------------------------


class GenreService:
    """The GenreService class with necessary business logic"""
    def __init__(self, dao: GenreDAO):
        """The initialization of the GenreService class

        :param dao: an instance of GenreDAO class
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

    def create(self, genre_d):
        """The method creates a new record in the database

        :param genre_d: a dictionary with data to create the record

        :returns: a model with dota of created record
        """
        return self.dao.create(genre_d)

    def update(self, genre_d) -> None:
        """The method updates a record in the database

        :param genre_d: a dictionary with data to update
        """
        return self.dao.update(genre_d)

    def partially_update(self, genre_d) -> None:
        """The method partially updates a record in the database

        :param genre_d: a dictionary with data to update
        """
        genre = self.get_one(genre_d["id"])
        if "name" in genre_d:
            genre.name = genre_d.get("name")
        self.dao.update(genre)

    def delete(self, rid) -> None:
        """The method deletes a record from the database

        :param rid: an id of the deleted record
        """
        self.dao.delete(rid)
