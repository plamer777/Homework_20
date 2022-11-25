"""The unit contains the TestDirectorService class and additional logic to
test the DirectorService class"""
from unittest.mock import MagicMock
import pytest
from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService
from tests.services.service_utils import check_single_model
# ------------------------------------------------------------------------


@pytest.fixture
def test_database() -> dict:
    """This fixture provides a test data for DirectorDAO

    :returns: A dictionary containing Director models
    """
    director_1 = Director(id=1, name='Джеймс Камерон')
    director_2 = Director(id=2, name='Люк Бессон')
    director_3 = Director(id=3, name='Стивен Спилберг')
    director_21 = Director(id=21, name='Квентин Тарантино')

    return {1: director_1, 2: director_2, 3: director_3, 21: director_21}


@pytest.fixture
def test_json() -> tuple:
    """This fixture provides test dictionaries to test create and update
    methods of DirectorDAO

    :returns: a tuple with two test dictionaries
    """
    json_data = {
        "id": 21,
        "name": "Квентин Тарантино"

    }

    json_data_update = {
        "id": 21,
        "name": "Федор Бондарчук"
    }

    return json_data, json_data_update


@pytest.fixture
def update_director(test_database, test_json) -> None:
    """This fixture provides serves to replace the update method of DirectorDao

    :param test_database: the fixture with test database data
    :param test_json: the fixture with test json data
    """
    updated_director = test_database.get(21)

    if updated_director:

        for key in test_json[1]:
            exec(f"updated_director.{key} = test_json[1]['{key}']")

        test_database[21] = updated_director


@pytest.fixture
def test_dao(test_database, update_director) -> DirectorDAO:
    """This fixture configures a DirectorDAO to work without using the
    database

    :param test_database: the fixture with test database data
    :returns: the configured instance of DirectorDAO
    """
    director_dao = DirectorDAO(None)

    director_dao.get_all = MagicMock(return_value=[*test_database.values()])
    director_dao.get_one = MagicMock(side_effect=test_database.get)
    director_dao.create = MagicMock(return_value=test_database.get(21))
    director_dao.update = MagicMock(side_effect=update_director)
    director_dao.delete = MagicMock()

    return director_dao
# -----------------------------------------------------------------------


class TestDirectorService:
    """The TestDirectorService class provides a logic to test all methods of
    DirectorService class"""
    @pytest.fixture(autouse=True)
    def service(self, test_dao) -> None:
        """The fixture serves to DirectorService in the class' field

        :param test_dao: the configured instance of DirectorDAO
        """
        self.service = DirectorService(test_dao)

    def test_get_one(self, test_database) -> None:
        """This method tests 'get_one' method of DirectorService

        :param test_database: the fixture with test database data
        """
        for director_id in range(1, 4):

            director = self.service.get_one(director_id)
            check_single_model(director, test_database.get(director_id),
                               Director)

    def test_get_all(self, test_database) -> None:
        """This method tests 'get_all' method of DirectorService

        :param test_database: the fixture with test database
        """
        directors = self.service.get_all()

        assert len(directors) == len(test_database), 'Получены не все фильмы'
        assert type(directors) == list, 'Неверные тип данных'

        for director, valid_director in zip(directors, test_database.values()):
            # this function checks if each received record is correct
            check_single_model(director, valid_director, Director)

    def test_create(self, test_database, test_json) -> None:
        """This method tests 'create' method of DirectorService

        :param test_database: the fixture with test database data
        :param test_json: the fixture with test dictionaries
        """
        result = self.service.create(test_json[0])
        valid_director = test_database.get(test_json[0].get("id"))
        check_single_model(result, valid_director, Director)

    def test_update(self, test_database, test_json) -> None:
        """This method tests 'update' method of DirectorService

        :param test_json: the fixture with test dictionaries
        """
        self.service.update(test_json[1])
        result = self.service.get_one(test_json[1].get("id"))
        check_single_model(result, test_database.get(result.id), Director)

    def test_partially_update(self, test_json) -> None:
        """This method tests 'partially_update' method of DirectorService

        :param test_json: the fixture with test dictionaries
        """
        self.service.partially_update(test_json[1])

    def test_delete(self) -> None:
        """This method tests 'delete' method of DirectorService"""
        self.service.delete(21)
