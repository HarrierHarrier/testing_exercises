import datetime

from freezegun import freeze_time
import pytest

from functions.level_1.two_date_parser import compose_datetime_from


@freeze_time('2023-01-01')
def test__compose_datetime_from__date_str_tomorow():
    test_value = datetime.datetime.now() + datetime.timedelta(days=1)

    value = compose_datetime_from('tomorrow', '00:00')

    assert value == test_value


@freeze_time('2023-01-01')
def test__compose_datetime_from__date_str_not_tomorow():
    test_value = datetime.datetime.now()

    value = compose_datetime_from('not tomorrow', '00:00')

    assert value == test_value


def test__compose_datetime_from__invalid_time_str_value():
    with pytest.raises(ValueError):
        compose_datetime_from('not tomorrow', '0911')


def test__compose_datetime_from__invalid_time_str_type():
    with pytest.raises(AttributeError):
        compose_datetime_from('not tomorrow', None)
