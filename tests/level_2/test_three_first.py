import pytest

from functions.level_2.three_first import first


@pytest.mark.parametrize(
    ("items", "expected_result"),
    [
        ([1, 2, 3], 1),
        ([2, 1, 2, 3], 2),
        ([3, 1, 2, 3], 3),
    ]
)
def test__first__get_first_element(items, expected_result):
    assert first(items) == expected_result


def test__first__get_custom_default():
    assert first([], 1) == 1


def test__first__raise_default_not_set():
    with pytest.raises(AttributeError):
        first([])
