# Вопросы:
#   1. Непонятно, зачем в parse_ineco_expense принимается несколько карт :с
#   2. Какой формат raw_sum предполагается?


import datetime
import decimal

from functions.level_1.four_bank_parser import (
    BankCard, SmsMessage, Expense, parse_ineco_expense
)


def test_parse_ineco_expense():
    # Значения параметров
    card_a = BankCard(last_digits='1029', owner='Alice')
    card_b = BankCard(last_digits='2910', owner='Bob')
    sms1 = SmsMessage(
        text='??? ??? 100.00 ???, 1029 01.01.23 04:20 Market authcode ****',
        author='Green Bank',
        sent_at=datetime.datetime(2023, 1, 2, 0, 0)
    )
    sms2 = SmsMessage(
        text='??? ??? 200.00 ???, 1029 01.01.23 04:20 Market',
        author='Yellow Bank',
        sent_at=datetime.datetime(2023, 1, 2, 0, 0)
    )
    sms3 = SmsMessage(
        text='??? ??? 300.00 ???, 1029 01.01.23 04:20 Central Market',
        author='Blue Bank',
        sent_at=datetime.datetime(2023, 1, 2, 0, 0)
    )
    sms4 = SmsMessage(
        text='??? ??? 400.00 ???, ***2910 01.01.23 04:20 Central Market',
        author='Red Bank',
        sent_at=datetime.datetime(2023, 1, 2, 0, 0)
    )
    # Проверки
    assert parse_ineco_expense(sms=sms1, cards=[card_a, card_b]) == Expense(
        amount=decimal.Decimal('100.00'),
        card=card_a,
        spent_in='Market',
        spent_at=datetime.datetime(2023, 1, 1, 4, 20)
    )
    assert parse_ineco_expense(sms=sms2, cards=[card_a, card_b]) == Expense(
        amount=decimal.Decimal('200.00'),
        card=card_a,
        spent_in='Market',
        spent_at=datetime.datetime(2023, 1, 1, 4, 20)
    )
    assert parse_ineco_expense(sms=sms3, cards=[card_a, card_b]) == Expense(
        amount=decimal.Decimal('300.00'),
        card=card_a,
        spent_in='Central Market',
        spent_at=datetime.datetime(2023, 1, 1, 4, 20)
    )
    assert parse_ineco_expense(sms=sms4, cards=[card_a, card_b]) == Expense(
        amount=decimal.Decimal('400.00'),
        card=card_b,
        spent_in='Central Market',
        spent_at=datetime.datetime(2023, 1, 1, 4, 20)
    )
