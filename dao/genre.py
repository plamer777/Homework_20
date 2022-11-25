"""There is the GenreDAO class in the unit providing access to the
database"""
from dao.model.genre import Genre
# ------------------------------------------------------------------------


class GenreDAO:
    """The GenreDAO class contains methods to get certain data from genre
    table"""
    def __init__(self, session) -> None:
        """The initialization of the class

        :param session: the current database's session
        """
        self.session = session

    def get_one(self, bid: int):
        """The method serves to get a single record from the genre table

        :param bid: the id of the searching record

        :returns: a model filled by data from the table
        """
        return self.session.query(Genre).get(bid)

    def get_all(self) -> list:
        """The method serves to get all records from the table

        :returns: a list of models filled by data from the table
        """
        return self.session.query(Genre).all()

    def create(self, genre_d: dict):
        """The method serves to create a new record in the table

        :param genre_d: a dictionary with data to create the record

        :returns: a model representing the created record
        """
        ent = Genre(**genre_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid: int) -> None:
        """The method serves to delete a record from the table

        :param rid: the id of the record to delete
        """
        genre = self.get_one(rid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, genre_d: dict) -> None:
        """The method serves to update a record in the table

        :param genre_d: a dictionary with data to update
        """
        genre = self.get_one(genre_d.get("id"))
        genre.name = genre_d.get("name")

        self.session.add(genre)
        self.session.commit()
