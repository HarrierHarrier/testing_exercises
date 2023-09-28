import datetime
import decimal

import pytest

from functions.level_1.four_bank_parser import (
    BankCard, SmsMessage, parse_ineco_expense
)


@pytest.mark.parametrize(
    'sms,cards,expected_result',
    [
        (
            SmsMessage(
                text='??? ??? 100.00 ???, 1029 01.01.23 04:20 Market authcode ****',
                author='Green Bank',
                sent_at=datetime.datetime(2023, 1, 2, 0, 0)
            ),
            [
                BankCard(last_digits='1029', owner='Alice'),
                BankCard(last_digits='2910', owner='Bob')
            ],
            decimal.Decimal('100.00')
        )
    ]
)
def test__parse_ineco_expense__amount(sms, cards, expected_result):
    assert parse_ineco_expense(sms, cards).amount == expected_result


@pytest.mark.parametrize(
    'sms,cards,expected_result',
    [
        (
            SmsMessage(
                text='??? ??? 100.00 ???, 1029 01.01.23 04:20 Market authcode ****',
                author='Green Bank',
                sent_at=datetime.datetime(2023, 1, 2, 0, 0)
            ),
            [
                BankCard(last_digits='1029', owner='Alice'),
                BankCard(last_digits='2910', owner='Bob')
            ],
            BankCard(last_digits='1029', owner='Alice')
        )
    ]
)
def test__parse_ineco_expense__card(sms, cards, expected_result):
    assert parse_ineco_expense(sms, cards).card == expected_result


@pytest.mark.parametrize(
    'sms,cards,expected_result',
    [
        (
            SmsMessage(
                text=(
                    '??? ??? 100.00 ???, 1029 01.01.23 04:20 Market'
                ),
                author='Green Bank',
                sent_at=datetime.datetime(2023, 1, 2, 0, 0)
            ),
            [
                BankCard(last_digits='1029', owner='Alice'),
                BankCard(last_digits='2910', owner='Bob')
            ],
            'Market'
        ),
        (
            SmsMessage(
                text=(
                    '??? ??? 100.00 ???, 1029 01.01.23 04:20 Local Market Nearby'
                ),
                author='Green Bank',
                sent_at=datetime.datetime(2023, 1, 2, 0, 0)
            ),
            [
                BankCard(last_digits='1029', owner='Alice'),
                BankCard(last_digits='2910', owner='Bob')
            ],
            'Local Market Nearby'
        ),
        (
            SmsMessage(
                text=(
                    '??? ??? 100.00 ???, 1029 01.01.23 04:20 Local Market Nearby'
                    ' authcode ****'
                ),
                author='Green Bank',
                sent_at=datetime.datetime(2023, 1, 2, 0, 0)
            ),
            [
                BankCard(last_digits='1029', owner='Alice'),
                BankCard(last_digits='2910', owner='Bob')
            ],
            'Local Market Nearby'
        )
    ],
    ids=[
        'one_word',
        'multiple_words',
        'with_authcode'
    ]
)
def test__parse_ineco_expense__spent_in(sms, cards, expected_result):
    assert parse_ineco_expense(sms, cards).spent_in == expected_result


@pytest.mark.parametrize(
    'sms,cards,expected_result',
    [
        (
            SmsMessage(
                text=(
                    '??? ??? 100.00 ???, 1029 01.01.23 04:20 Central Market '
                    'authcode ****'
                ),
                author='Green Bank',
                sent_at=datetime.datetime(2023, 1, 2, 0, 0)
            ),
            [
                BankCard(last_digits='1029', owner='Alice'),
                BankCard(last_digits='2910', owner='Bob')
            ],
            datetime.datetime(2023, 1, 1, 4, 20)
        )
    ]
)
def test__parse_ineco_expense__spent_at(sms, cards, expected_result):
    assert parse_ineco_expense(sms, cards).spent_at == expected_result
