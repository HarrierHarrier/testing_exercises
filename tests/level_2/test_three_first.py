import pytest

from functions.level_2.three_first import first, NOT_SET


@pytest.mark.parametrize(
    'items,default,expected_result',
    [
        ([1, 2, 3], NOT_SET, 1),
        ([], 1, 1),
    ],
    ids=[
        'get_first_element',
        'get_custom_default'
    ]
)
def test__first__success(items, default, expected_result):
    assert first(items, default) == expected_result


def test__first__raise_default_not_set():
    with pytest.raises(AttributeError):
        first([])
