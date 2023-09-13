from functions.level_1.one_gender import genderalize


def test_genderalize():
    # Проверки
    assert genderalize(
        verb_male='сделал', verb_female='сделала', gender='male'
    ) == 'сделал'
    assert genderalize(
        verb_male='сделал', verb_female='сделала', gender='female'
    ) == 'сделала'
    assert genderalize(
        verb_male='сделал', verb_female='сделала', gender='genderfluid'
    ) == 'сделала'
