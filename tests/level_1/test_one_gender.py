import pytest

from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(
    "verb_male,verb_female,gender,expected_result",
    [
        ('сделал', 'сделала', 'male', 'сделал'),
        ('сделал', 'сделала', 'female', 'сделала'),
        ('сделал', 'сделала', 'genderfluid', 'сделала'),
    ],
    ids=[
        'male_verb',
        'female_verb',
        'another_verb'
    ]
)
def test__genderalize(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) == expected_result
