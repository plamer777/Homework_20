"""The unit contains the TestGenreService class and additional logic to
test the GenreService class"""
from unittest.mock import MagicMock
import pytest
from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService
from tests.services.service_utils import check_single_model
# ------------------------------------------------------------------------


@pytest.fixture
def test_database() -> dict:
    """This fixture provides a test data for GenreDAO

    :returns: A dictionary containing Genre models
    """
    genre_1 = Genre(id=1, name='Комедия')
    genre_2 = Genre(id=2, name='Ужасы')
    genre_3 = Genre(id=3, name='Триллер')
    genre_21 = Genre(id=21, name='Мистика')

    return {1: genre_1, 2: genre_2, 3: genre_3, 21: genre_21}


@pytest.fixture
def test_json() -> tuple:
    """This fixture provides test dictionaries to test create and update
    methods of GenreDAO

    :returns: a tuple with two test dictionaries
    """
    json_data = {
        "id": 21,
        "name": "Мелодрама"

    }

    json_data_update = {
        "id": 21,
        "name": "Документальный"
    }

    return json_data, json_data_update


@pytest.fixture
def update_genre(test_database, test_json) -> None:
    """This fixture provides serves to replace the update method of GenreDao

    :param test_database: the fixture with test database data
    :param test_json: the fixture with test json data
    """
    updated_genre = test_database.get(21)

    if updated_genre:

        for key in test_json[1]:
            exec(f"updated_genre.{key} = test_json[1]['{key}']")

        test_database[21] = updated_genre


@pytest.fixture
def test_dao(test_database, update_genre) -> GenreDAO:
    """This fixture configures a GenreDAO to work without using the
    database

    :param test_database: the fixture with test database data
    :returns: the configured instance of GenreDAO
    """
    genre_dao = GenreDAO(None)

    genre_dao.get_all = MagicMock(return_value=[*test_database.values()])
    genre_dao.get_one = MagicMock(side_effect=test_database.get)
    genre_dao.create = MagicMock(return_value=test_database.get(21))
    genre_dao.update = MagicMock(side_effect=update_genre)
    genre_dao.delete = MagicMock()

    return genre_dao
# -----------------------------------------------------------------------


class TestGenreService:
    """The TestGenreService class provides a logic to test all methods of
    GenreService class"""

    @pytest.fixture(autouse=True)
    def service(self, test_dao) -> None:
        """The fixture serves to GenreService in the class' field

        :param test_dao: the configured instance of GenreDAO
        """
        self.service = GenreService(test_dao)

    def test_get_one(self, test_database) -> None:
        """This method tests 'get_one' method of GenreService

        :param test_database: the fixture with test database data
        """
        for genre_id in range(1, 4):
            genre = self.service.get_one(genre_id)
            check_single_model(genre, test_database.get(genre_id),
                               Genre)

    def test_get_all(self, test_database) -> None:
        """This method tests 'get_all' method of GenreService

        :param test_database: the fixture with test database
        """
        genres = self.service.get_all()

        assert len(genres) == len(test_database), 'Получены не все фильмы'
        assert type(genres) == list, 'Неверные тип данных'

        for genre, valid_genre in zip(genres, test_database.values()):
            # this function checks if each received record is correct
            check_single_model(genre, valid_genre, Genre)

    def test_create(self, test_database, test_json) -> None:
        """This method tests 'create' method of GenreService

        :param test_database: the fixture with test database data
        :param test_json: the fixture with test dictionaries
        """
        result = self.service.create(test_json[0])
        valid_genre = test_database.get(test_json[0].get("id"))
        check_single_model(result, valid_genre, Genre)

    def test_update(self, test_database, test_json) -> None:
        """This method tests 'update' method of GenreService

        :param test_json: the fixture with test dictionaries
        """
        self.service.update(test_json[1])
        result = self.service.get_one(test_json[1]['id'])
        check_single_model(result,test_database.get(result.id), Genre)

    def test_partially_update(self, test_json) -> None:
        """This method tests 'partially_update' method of GenreService

        :param test_json: the fixture with test dictionaries
        """
        self.service.partially_update(test_json[1])

    def test_delete(self) -> None:
        """This method tests 'delete' method of GenreService"""
        self.service.delete(21)
