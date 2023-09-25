import pytest

from functions.level_2.three_first import first


def test__first__get_first_element():
    assert first([1, 2, 3]) == 1


def test__first__get_custom_default():
    assert first([], 1) == 1


def test__first__raise_default_not_set():
    with pytest.raises(AttributeError):
        first([])
