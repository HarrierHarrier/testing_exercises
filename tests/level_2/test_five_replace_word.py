import pytest

from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize(
    "replace_from,replace_to",
    [
        ("hello", "goodbye"),
        ("world", "goodbye"),
    ]
)
def test__replace_word__old_word_removed(replace_from, replace_to):
    replaced_text = replace_word("hello world", replace_from, replace_to)

    assert replace_from not in replaced_text


@pytest.mark.parametrize(
    "replace_from,replace_to",
    [
        ("hello", "goodbye"),
        ("world", "goodbye"),
    ]
)
def test_replace_word__new_word_appeared(replace_from, replace_to):
    replaced_text = replace_word("hello world", replace_from, replace_to)

    assert replace_to in replaced_text


@pytest.mark.parametrize(
    "text,replace_from,replace_to,expected_result",
    [
        ("hello world", "hello", "goodbye", "goodbye world"),
        ("hello world", "world", "goodbye", "hello goodbye"),
    ]
)
def test__replace_word__one_appearence_replaced(
    text, replace_from, replace_to, expected_result
):
    assert replace_word(text, replace_from, replace_to) == expected_result


@pytest.mark.parametrize(
    "text,replace_from,replace_to,expected_result",
    [
        ("hello world hello", "hello", "goodbye", "goodbye world goodbye"),
        ("hello world world", "world", "goodbye", "hello goodbye goodbye"),
    ]
)
def test__replace_word__multiple_appearence_replaced(
    text, replace_from, replace_to, expected_result
):
    assert replace_word(text, replace_from, replace_to) == expected_result


def test__replace_word__case_sensitive_replace_from():
    assert replace_word("Hello world", "hello", "goodbye") == "goodbye world"


def test__replace_word__case_sensitive_replace_to():
    assert replace_word("hello world", "hello", "Goodbye") == "Goodbye world"
