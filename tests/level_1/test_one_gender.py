import pytest

from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(
    "verb_male,verb_female",
    [
        ("сделал", "сделала"),
        ("сказал", "сказала"),
        ("написал", "написала"),
    ]
)
def test__genderalize__check_male_verb(verb_male, verb_female):
    assert genderalize(
        verb_male, verb_female, gender="male"
    ) == verb_male


@pytest.mark.parametrize(
    "verb_male,verb_female",
    [
        ("сделал", "сделала"),
        ("сказал", "сказала"),
        ("написал", "написала"),
    ]
)
def test__genderalize__check_female_verb(verb_male, verb_female):
    assert genderalize(
        verb_male, verb_female, gender="female"
    ) == verb_female


def test__genderalize__check_another_verb():
    assert genderalize(
        verb_male="сделал", verb_female="сделала", gender="genderfluid"
    ) == "сделала"
