import pytest

from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize(
    "text,replace_from,replace_to,expected_result",
    [
        ('hello world', 'hello', 'goodbye', 'goodbye world'),
        ('hello world hello', 'hello', 'goodbye', 'goodbye world goodbye'),
        ('Hello world', 'hello', 'goodbye', 'goodbye world'),
        ('hello world', 'hello', 'Goodbye', 'Goodbye world'),
    ],
    ids=[
        'one_appearence_replaced',
        'multiple_appearence_replaced',
        'case_sensitive_replace_from',
        'case_sensitive_replace_to',
    ]
)
def test__replace_word__success(
    text, replace_from, replace_to, expected_result
):
    assert replace_word(text, replace_from, replace_to) == expected_result


def test__replace_word__old_word_removed():
    old_word = 'hello'

    replaced_text = replace_word('hello world', old_word, 'goodbye')

    assert old_word not in replaced_text


def test_replace_word__new_word_appeared():
    new_word = 'goodbye'

    replaced_text = replace_word('hello world', 'hello', new_word)

    assert new_word in replaced_text
