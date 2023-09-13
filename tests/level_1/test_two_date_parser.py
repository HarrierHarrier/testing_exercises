import datetime

from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_from():
    # Динамические значения
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    # Проверки
    assert compose_datetime_from('tomorrow', '09:11') == datetime.datetime(
        tomorrow.year,
        tomorrow.month,
        tomorrow.day,
        9,
        11
    )
    assert compose_datetime_from('not tomorrow', '09:11') == datetime.datetime(
        today.year,
        today.month,
        today.day,
        9,
        11
    )
