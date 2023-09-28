import datetime

from freezegun import freeze_time
import pytest

from functions.level_1.two_date_parser import compose_datetime_from


@freeze_time('2023-01-01')
@pytest.mark.parametrize(
    "date_str,time_str,expected_result",
    [
        ('tomorrow', '00:00', datetime.datetime(2023, 1, 2, 0, 0)),
        ('not tomorrow', '00:00', datetime.datetime(2023, 1, 1, 0, 0)),
    ],
    ids=[
        'date_str_tomorow',
        'date_str_not_tomorow',
    ]
)
def test__compose_datetime_from__success(date_str, time_str, expected_result):
    assert compose_datetime_from(date_str, time_str) == expected_result


@pytest.mark.parametrize(
    "date_str,time_str,expected_raise",
    [
        ('not tomorrow', '0911', pytest.raises(ValueError)),
        ('not tomorrow', None, pytest.raises(AttributeError)),
    ],
    ids=[
        'invalid_time_str_value',
        'invalid_time_str_type',
    ]
)
def test__compose_datetime_from__fail(date_str, time_str, expected_raise):
    with expected_raise:
        compose_datetime_from(date_str, time_str)
