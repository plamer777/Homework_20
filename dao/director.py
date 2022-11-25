"""There is the DirectorDAO class in the unit providing access to the
database"""
from dao.model.director import Director
# ------------------------------------------------------------------------


class DirectorDAO:
    """The DirectorDAO class contains methods to get certain data from
    director table"""
    def __init__(self, session) -> None:
        """The initialization of the class

        :param session: the current database's session
        """
        self.session = session

    def get_one(self, bid: int):
        """The method serves to get a single record from the director table

        :param bid: the id of the searching record

        :returns: a model filled by data from the table
        """
        return self.session.query(Director).get(bid)

    def get_all(self) -> list:
        """The method serves to get all records from the table

        :returns: a list of models filled by data from the table
        """
        return self.session.query(Director).all()

    def create(self, director_d: dict):
        """The method serves to create a new record in the table

        :param director_d: a dictionary with data to create the record

        :returns: a model representing the created record
        """
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid: int) -> None:
        """The method serves to delete a record from the table

        :param rid: the id of the record to delete
        """
        director = self.get_one(rid)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_d: dict) -> None:
        """The method serves to update a record in the table

        :param director_d: a dictionary with data to update
        """
        director = self.get_one(director_d.get("id"))
        director.name = director_d.get("name")

        self.session.add(director)
        self.session.commit()
