"""The unit contains the MovieService class providing a business logic to
interact with movies' data"""
from dao.movie import MovieDAO
# ------------------------------------------------------------------------


class MovieService:
    """The MovieService class with necessary business logic"""
    def __init__(self, dao: MovieDAO) -> None:
        """The initialization of the MovieService class

        :param dao: an instance of MovieDAO class
        """
        self.dao = dao

    def get_one(self, bid):
        """The method returns a single record found in the database

        :param bid: the id of the searching record

        :returns: a model with dota of found record
        """
        return self.dao.get_one(bid)

    def get_all(self):
        """The method returns a list of records found in the database

        :returns: a list of models
        """
        return self.dao.get_all()
    
    def create(self, movie_d):
        """The method creates a new record in the database

        :param movie_d: a dictionary with data to create the record

        :returns: a model with dota of created record
        """
        return self.dao.create(movie_d)

    def update(self, movie_d) -> None:
        """The method updates a record in the database

        :param movie_d: a dictionary with data to update
        """
        return self.dao.update(movie_d)

    def partially_update(self, movie_d) -> None:
        """The method partially updates a record in the database

        :param movie_d: a dictionary with data to update
        """
        movie = self.get_one(movie_d["id"])
        if "title" in movie_d:
            movie.title = movie_d.get("title")
        if "description" in movie_d:
            movie.description = movie_d.get("description")
        if "trailer" in movie_d:
            movie.trailer = movie_d.get("trailer")
        if "year" in movie_d:
            movie.year = movie_d.get("year")
        if "rating" in movie_d:
            movie.rating = movie_d.get("rating")
        if "genre_id" in movie_d:
            movie.genre_id = movie_d.get("genre_id")
        if "director_id" in movie_d:
            movie.director_id = movie_d.get("director_id")
        self.dao.update(movie)

    def delete(self, rid) -> None:
        """The method deletes a record from the database

        :param rid: an id of the deleted record
        """
        self.dao.delete(rid)
