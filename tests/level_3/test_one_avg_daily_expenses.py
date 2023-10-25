from decimal import Decimal
from statistics import StatisticsError
import datetime

import pytest

from functions.level_3.models import Currency
from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses


def test__calculate_average_daily_expenses__empty_list():
    with pytest.raises(StatisticsError):
        calculate_average_daily_expenses([])


def test__calculate_average_daily_expenses__non_empty_list_one_date(get_expense_by_amount_value):
    amounts = [Decimal(i) for i in (20, 15, 25, 100)]
    expenses = [get_expense_by_amount_value(amount, Currency("RUB")) for amount in amounts]

    assert calculate_average_daily_expenses(expenses) == sum(amounts)


def test__calculate_average_daily_expenses__non_empty_list_multiple_dates(get_expense_by_spent_at_value):
    timestamps = [datetime.datetime(2023, 1, i) for i in range(1, 5)]
    expenses = [get_expense_by_spent_at_value(spent_at) for spent_at in timestamps]
    expected_result = sum(item.amount for item in expenses) / len(expenses)

    assert calculate_average_daily_expenses(expenses) == expected_result


@pytest.mark.xfail(reason="Implementation does not consider different currencies")
def test__calculate_average_daily_expenses__different_currencies(get_expense_by_amount_value):
    amounts = [Decimal(i) for i in (20, 15, 25, 100)]
    values = list(zip(
        amounts,
        [Currency("RUB") if i % 2 == 0 else Currency("USD")
         for i in range(len(amounts))]
    ))
    expenses = [get_expense_by_amount_value(amount, currency) for amount, currency in values]

    with pytest.raises(Exception):
        calculate_average_daily_expenses(expenses)
