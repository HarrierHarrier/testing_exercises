import datetime

from freezegun import freeze_time
import pytest

from functions.level_1.two_date_parser import compose_datetime_from


@freeze_time("2023-01-01")
@pytest.mark.parametrize(
    "time_str",
    [
        "00:00",
        "04:20",
        "12:36",
    ]
)
def test__compose_datetime_from__time_str_prased(time_str):
    test_value = datetime.datetime.strptime(
        f"2023-01-02 {time_str}", "%Y-%m-%d %H:%M"
    )

    assert compose_datetime_from("tomorrow", time_str) == test_value


@freeze_time("2023-01-01")
@pytest.mark.parametrize(
    "date_str",
    [
        "not tomorrow",
        "something",
        "something else",
    ]
)
def test__compose_datetime_from__date_str_not_tomorow(date_str):
    assert compose_datetime_from(date_str, "00:00") == datetime.datetime.now()


@pytest.mark.parametrize(
    "time_str",
    [
        "0420",
        "hello world",
    ]
)
def test__compose_datetime_from__invalid_time_str_value(time_str):
    with pytest.raises(ValueError):
        compose_datetime_from("not tomorrow", time_str)
