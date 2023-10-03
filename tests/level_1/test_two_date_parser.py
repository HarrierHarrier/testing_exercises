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
def test__compose_datetime_from__date_str_tomorow(time_str):
    time_value = time_str.split(":")
    test_value = datetime.datetime.now() + datetime.timedelta(
        days=1, hours=int(time_value[0]), minutes=int(time_value[1])
    )

    value = compose_datetime_from("tomorrow", time_str)

    assert value == test_value


@freeze_time("2023-01-01")
@pytest.mark.parametrize(
    "date_str,time_str",
    [
        ("not tomorrow", "00:00"),
        ("something", "04:20"),
        ("something else", "12:36"),
    ]
)
def test__compose_datetime_from__date_str_not_tomorow(date_str, time_str):
    time_value = time_str.split(":")
    test_value = datetime.datetime.now() + datetime.timedelta(
        hours=int(time_value[0]), minutes=int(time_value[1])
    )

    value = compose_datetime_from(date_str, time_str)

    assert value == test_value


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
