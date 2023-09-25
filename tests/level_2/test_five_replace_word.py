from functions.level_2.five_replace_word import replace_word


def test__replace_word__old_word_removed():
    old_word = 'hello'

    replaced_text = replace_word('hello world', old_word, 'goodbye')

    assert old_word not in replaced_text


def test_replace_word__new_word_appeared():
    new_word = 'goodbye'

    replaced_text = replace_word('hello world', 'hello', new_word)

    assert new_word in replaced_text


def test__replace_word__one_appearence_replaced():
    assert replace_word('hello world', 'hello', 'goodbye') == 'goodbye world'


def test__replace_word__multiple_appearence_replaced():
    assert replace_word(
        'hello world hello', 'hello', 'goodbye'
    ) == 'goodbye world goodbye'
