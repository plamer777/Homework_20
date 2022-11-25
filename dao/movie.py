"""There is the MovieDAO class in the unit providing access to the
database"""
from dao.model.movie import Movie
# ------------------------------------------------------------------------


class MovieDAO:
    """The MovieDAO class contains methods to get certain data from movie
    table"""
    def __init__(self, session) -> None:
        """The initialization of the class

        :param session: the current database's session
        """
        self.session = session

    def get_one(self, bid: int):
        """The method serves to get a single record from the movie table

        :param bid: the id of the searching record

        :returns: a model filled by data from the table
        """
        return self.session.query(Movie).get(bid)

    def get_all(self) -> list:
        """The method serves to get all records from the table

        :returns: a list of models filled by data from the table
        """
        return self.session.query(Movie).all()

    def create(self, movie_d: dict):
        """The method serves to create a new record in the table

        :param movie_d: a dictionary with data to create the record

        :returns: a model representing the created record
        """
        ent = Movie(**movie_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid: int) -> None:
        """The method serves to delete a record from the table

        :param rid: the id of the record to delete
        """
        movie = self.get_one(rid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_d: dict) -> None:
        """The method serves to update a record in the table

        :param movie_d: a dictionary with data to update
        """
        movie = self.get_one(movie_d.get("id"))
        movie.title = movie_d.get("title")
        movie.description = movie_d.get("description")
        movie.trailer = movie_d.get("trailer")
        movie.year = movie_d.get("year")
        movie.rating = movie_d.get("rating")
        movie.genre_id = movie_d.get("genre_id")
        movie.director_id = movie_d.get("director_id")

        self.session.add(movie)
        self.session.commit()
