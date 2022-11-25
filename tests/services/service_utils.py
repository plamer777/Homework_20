"""The unit contains functions for testing purposes"""


def check_single_model(checked_data, valid_data, model_class) -> None:
    """This function checks if received data exists, valid and an instance
    of its model class

    :param checked_data: a model instance to test
    :param valid_data: a model taken from the test database
    :param model_class: the class of the checked_data
    """
    assert checked_data is not None, 'Данные не получены'
    assert checked_data == valid_data, 'Данные не совпадают'
    assert isinstance(checked_data, model_class), 'Класс модели неверен'
