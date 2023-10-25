from decimal import Decimal
import datetime

import pytest

from functions.level_3 import models


@pytest.fixture
def card():
    return models.BankCard(
        last_digits="1234",
        owner="Alice"
    )


@pytest.fixture
def spent_in():
    return "Cool service"


@pytest.fixture
def category():
    return models.ExpenseCategory("ONLINE_SUBSCRIPTIONS")


@pytest.fixture
def get_expense_by_amount_value(card, spent_in, category):
    def func(
        amount: Decimal, currency: models.Currency
    ) -> models.Expense:
        return models.Expense(
            amount=amount,
            currency=currency,
            card=card,
            spent_in=spent_in,
            spent_at=datetime.datetime(2023, 1, 1, 0, 0),
            category=category
        )
    return func


@pytest.fixture
def get_expense_by_spent_at_value(card, spent_in, category):
    def func(
        spent_at: datetime.datetime
    ) -> models.Expense:
        return models.Expense(
            amount=Decimal("25.00"),
            currency=models.Currency("RUB"),
            card=card,
            spent_in=spent_in,
            spent_at=spent_at,
            category=category
        )
    return func
