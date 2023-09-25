from functions.level_1.one_gender import genderalize


def test__genderalize__check_male_verb():
    assert genderalize(
        verb_male='сделал', verb_female='сделала', gender='male'
    ) == 'сделал'


def test__genderalize__check_female_verb():
    assert genderalize(
        verb_male='сделал', verb_female='сделала', gender='female'
    ) == 'сделала'


def test__genderalize__check_another_verb():
    assert genderalize(
        verb_male='сделал', verb_female='сделала', gender='genderfluid'
    ) == 'сделала'
