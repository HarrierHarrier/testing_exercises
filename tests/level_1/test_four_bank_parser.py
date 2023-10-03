import datetime
import decimal

import pytest

from functions.level_1.four_bank_parser import (
    BankCard, SmsMessage, parse_ineco_expense
)


@pytest.mark.parametrize(
    "amount",
    [
        100.0,
        52.0,
        0.25
    ]
)
def test__parse_ineco_expense__amount_parsed_correctly(amount: float):
    card_a = BankCard(last_digits="1029", owner="Alice")
    card_b = BankCard(last_digits="2910", owner="Bob")
    sms = SmsMessage(
        text=f"??? ??? {amount:.2f} ???, 1029 01.01.23 04:20 Market authcode ****",
        author="Green Bank",
        sent_at=datetime.datetime(2023, 1, 2, 0, 0)
    )

    value = parse_ineco_expense(sms=sms, cards=[card_a, card_b])

    assert value.amount == decimal.Decimal(f"{amount:.2f}")


@pytest.mark.parametrize(
    "card",
    [
        BankCard(last_digits="1029", owner="Alice"),
        BankCard(last_digits="2910", owner="Bob"),
    ]
)
def test__parse_ineco_expense__card_parsed_correctly(card: BankCard):
    card_a = BankCard(last_digits="1029", owner="Alice")
    card_b = BankCard(last_digits="2910", owner="Bob")
    sms = SmsMessage(
        text=f"??? ??? 100.00 ???, {card.last_digits} 01.01.23 04:20 Market authcode ****",
        author="Green Bank",
        sent_at=datetime.datetime(2023, 1, 2, 0, 0)
    )

    value = parse_ineco_expense(sms=sms, cards=[card_a, card_b])

    assert value.card == card


@pytest.mark.parametrize(
    "spent_in",
    [
        "Market",
        "Coffeshop",
        "Bakery",
    ]
)
def test__parse_ineco_expense__spent_in_one_word_parsed_correctly(spent_in: str):
    card_a = BankCard(last_digits="1029", owner="Alice")
    card_b = BankCard(last_digits="2910", owner="Bob")
    sms = SmsMessage(
        text=(
            f"??? ??? 100.00 ???, 1029 01.01.23 04:20 {spent_in}"
        ),
        author="Green Bank",
        sent_at=datetime.datetime(2023, 1, 2, 0, 0)
    )

    value = parse_ineco_expense(sms=sms, cards=[card_a, card_b])

    assert value.spent_in == spent_in


@pytest.mark.parametrize(
    "spent_in",
    [
        "Local Market Nearby",
        "Famous Coffeshop",
        "Local Bakery",
    ]
)
def test__parse_ineco_expense__spent_in_multiple_words_parsed_correctly(spent_in: str):
    card_a = BankCard(last_digits="1029", owner="Alice")
    card_b = BankCard(last_digits="2910", owner="Bob")
    sms = SmsMessage(
        text=(
            f"??? ??? 100.00 ???, 1029 01.01.23 04:20 {spent_in}"
        ),
        author="Green Bank",
        sent_at=datetime.datetime(2023, 1, 2, 0, 0)
    )

    value = parse_ineco_expense(sms=sms, cards=[card_a, card_b])

    assert value.spent_in == spent_in


@pytest.mark.parametrize(
    "spent_in",
    [
        "Market",
        "Coffeshop",
        "Bakery",
        "Local Market Nearby",
        "Famous Coffeshop",
        "Local Bakery",
    ]
)
def test__parse_ineco_expense__spent_in_with_authcode_parsed_correctly(spent_in: str):
    card_a = BankCard(last_digits="1029", owner="Alice")
    card_b = BankCard(last_digits="2910", owner="Bob")
    sms = SmsMessage(
        text=(
            f"??? ??? 100.00 ???, 1029 01.01.23 04:20 {spent_in} authcode ****"
        ),
        author="Green Bank",
        sent_at=datetime.datetime(2023, 1, 2, 0, 0)
    )

    value = parse_ineco_expense(sms=sms, cards=[card_a, card_b])

    assert value.spent_in == spent_in


@pytest.mark.parametrize(
    "spent_at",
    [
        "01.01.23 04:20",
        "05.11.15 10:34",
        "28.03.28 12:00",
    ]
)
def test__parse_ineco_expense__spent_at_parsed_correctly(spent_at: str):
    card_a = BankCard(last_digits="1029", owner="Alice")
    card_b = BankCard(last_digits="2910", owner="Bob")
    sms = SmsMessage(
        text=(
            f"??? ??? 100.00 ???, 1029 {spent_at} Central Market authcode ****"
        ),
        author="Green Bank",
        sent_at=datetime.datetime(2023, 1, 2, 0, 0)
    )
    value = parse_ineco_expense(sms=sms, cards=[card_a, card_b])

    assert value.spent_at == datetime.datetime.strptime(spent_at, "%d.%m.%y %H:%M")
