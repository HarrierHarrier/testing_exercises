import datetime
import decimal

from functions.level_1.four_bank_parser import (
    BankCard, SmsMessage, parse_ineco_expense
)


def test__parse_ineco_expense__amount_parsed_correctly():
    card_a = BankCard(last_digits='1029', owner='Alice')
    card_b = BankCard(last_digits='2910', owner='Bob')
    sms = SmsMessage(
        text='??? ??? 100.00 ???, 1029 01.01.23 04:20 Market authcode ****',
        author='Green Bank',
        sent_at=datetime.datetime(2023, 1, 2, 0, 0)
    )

    value = parse_ineco_expense(sms=sms, cards=[card_a, card_b])

    assert value.amount == decimal.Decimal('100.00')


def test__parse_ineco_expense__card_parsed_correctly():
    card_a = BankCard(last_digits='1029', owner='Alice')
    card_b = BankCard(last_digits='2910', owner='Bob')
    sms = SmsMessage(
        text='??? ??? 100.00 ???, 1029 01.01.23 04:20 Market authcode ****',
        author='Green Bank',
        sent_at=datetime.datetime(2023, 1, 2, 0, 0)
    )

    value = parse_ineco_expense(sms=sms, cards=[card_a, card_b])

    assert value.card == card_a


def test__parse_ineco_expense__spent_in_one_word_parsed_correctly():
    card_a = BankCard(last_digits='1029', owner='Alice')
    card_b = BankCard(last_digits='2910', owner='Bob')
    sms = SmsMessage(
        text=(
            '??? ??? 100.00 ???, 1029 01.01.23 04:20 Market'
        ),
        author='Green Bank',
        sent_at=datetime.datetime(2023, 1, 2, 0, 0)
    )

    value = parse_ineco_expense(sms=sms, cards=[card_a, card_b])

    assert value.spent_in == 'Market'


def test__parse_ineco_expense__spent_in_multiple_words_parsed_correctly():
    card_a = BankCard(last_digits='1029', owner='Alice')
    card_b = BankCard(last_digits='2910', owner='Bob')
    sms = SmsMessage(
        text=(
            '??? ??? 100.00 ???, 1029 01.01.23 04:20 Local Market Nearby'
        ),
        author='Green Bank',
        sent_at=datetime.datetime(2023, 1, 2, 0, 0)
    )

    value = parse_ineco_expense(sms=sms, cards=[card_a, card_b])

    assert value.spent_in == 'Local Market Nearby'


def test__parse_ineco_expense__spent_in_with_authcode_parsed_correctly():
    card_a = BankCard(last_digits='1029', owner='Alice')
    card_b = BankCard(last_digits='2910', owner='Bob')
    sms = SmsMessage(
        text=(
            '??? ??? 100.00 ???, 1029 01.01.23 04:20 Local Market Nearby'
            ' authcode ****'
        ),
        author='Green Bank',
        sent_at=datetime.datetime(2023, 1, 2, 0, 0)
    )

    value = parse_ineco_expense(sms=sms, cards=[card_a, card_b])

    assert value.spent_in == 'Local Market Nearby'


def test__parse_ineco_expense__spent_at_parsed_correctly():
    card_a = BankCard(last_digits='1029', owner='Alice')
    card_b = BankCard(last_digits='2910', owner='Bob')
    sms = SmsMessage(
        text=(
            '??? ??? 100.00 ???, 1029 01.01.23 04:20 Central Market '
            'authcode ****'
        ),
        author='Green Bank',
        sent_at=datetime.datetime(2023, 1, 2, 0, 0)
    )
    value = parse_ineco_expense(sms=sms, cards=[card_a, card_b])

    assert value.spent_at == datetime.datetime(2023, 1, 1, 4, 20)
