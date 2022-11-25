"""The unit contains the TestMovieService class and additional logic to
test the MovieService class"""
from unittest.mock import MagicMock
import pytest
from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService
from tests.services.service_utils import check_single_model
# ------------------------------------------------------------------------


@pytest.fixture
def test_database() -> dict:
    """This fixture provides a test data for MovieDAO

    :returns: A dictionary containing Movie models
    """
    movie_1 = Movie(id=1, title='Поворот не туда 1', year=2000, rating=8.1)
    movie_2 = Movie(id=2, title='Поворот не туда 2', year=2002, rating=7.8)
    movie_3 = Movie(id=3, title='Поворот не туда 3', year=2005, rating=7.5)
    movie_21 = Movie(id=21, title='Правда или действие', year=2010, rating=9.0)

    return {1: movie_1, 2: movie_2, 3: movie_3, 21: movie_21}


@pytest.fixture
def test_json() -> tuple:
    """This fixture provides test dictionaries to test create and update
    methods of MovieDAO

    :returns: a tuple with two test dictionaries
    """
    json_data = {
        "id": 21,
        "title": "Правда или действие",
        "year": 2010,
        "rating": 9.0
    }

    json_data_update = {
        "id": 21,
        "title": "Гром в Раю",
        "year": 1990,
        "rating": 10.0
    }

    return json_data, json_data_update


@pytest.fixture
def update_movie(test_database, test_json) -> None:
    """This fixture provides serves to replace the update method of MovieDao

    :param test_database: the fixture with test database data
    :param test_json: the fixture with test json data
    """
    updated_movie = test_database.get(21)

    if updated_movie:

        for key in test_json[1]:

            exec(f"updated_movie.{key} = test_json[1]['{key}']")

        test_database[21] = updated_movie


@pytest.fixture
def test_dao(test_database, update_movie) -> MovieDAO:
    """This fixture configures a MovieDAO to work without using the
    database

    :param test_database: the fixture with test database data
    :returns: the configured instance of MovieDAO
    """
    movie_dao = MovieDAO(None)

    movie_dao.create = MagicMock(return_value=test_database[21])
    movie_dao.get_all = MagicMock(return_value=[*test_database.values()])
    movie_dao.get_one = MagicMock(side_effect=test_database.get)
    movie_dao.update = MagicMock(side_effect=update_movie)
    movie_dao.delete = MagicMock()

    return movie_dao
# -----------------------------------------------------------------------


class TestMovieService:
    """The TestMovieService class provides a logic to test all methods of
    MovieService class"""
    @pytest.fixture(autouse=True)
    def service(self, test_dao) -> None:
        """The fixture serves to MovieService in the class' field

        :param test_dao: the configured instance of MovieDAO
        """
        self.service = MovieService(test_dao)

    def test_get_one(self, test_database) -> None:
        """This method tests 'get_one' method of MovieService

        :param test_database: the fixture with test database data
        """
        for movie_id in range(1, 4):

            movie = self.service.get_one(movie_id)
            check_single_model(movie, test_database.get(movie_id), Movie)

    def test_get_all(self, test_database) -> None:
        """This method tests 'get_all' method of MovieService

        :param test_database: the fixture with test database
        """
        movies = self.service.get_all()

        assert len(movies) == len(test_database), 'Получены не все фильмы'
        assert type(movies) == list, 'Неверные тип данных'

        for movie, valid_movie in zip(movies, test_database.values()):
            check_single_model(movie, valid_movie, Movie)

    def test_create(self, test_database, test_json) -> None:
        """This method tests 'create' method of MovieService

        :param test_database: the fixture with test database data
        :param test_json: the fixture with test dictionaries
        """
        result = self.service.create(test_json[0])
        added_movie = test_database.get(test_json[0].get("id"))
        check_single_model(result, added_movie, Movie)

    def test_update(self, test_json, test_database) -> None:
        """This method tests 'update' method of MovieService

        :param test_json: the fixture with test dictionaries
        """
        self.service.update(test_json[1])
        updated_movie = self.service.get_one(test_json[1].get("id"))
        check_single_model(updated_movie, test_database.get(updated_movie.id),
                           Movie)

    def test_partially_update(self, test_json) -> None:
        """This method tests 'partially_update' method of MovieService

        :param test_json: the fixture with test dictionaries
        """
        self.service.partially_update(test_json[1])

    def test_delete(self) -> None:
        """This method tests 'delete' method of MovieService"""
        self.service.delete(21)
