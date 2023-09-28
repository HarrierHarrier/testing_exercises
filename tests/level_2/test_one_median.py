import pytest

from functions.level_2.one_median import get_median_value


@pytest.mark.parametrize(
    "items,expected_result",
    [
        ([], None),
        pytest.param([11, 9, 3, 5, 5], 5, marks=pytest.mark.xfail(reason='wrong implementation')),
        pytest.param([1, 3, 5, 7], 4, marks=pytest.mark.xfail(reason='wrong implementation')),
    ],
    ids=[
        'empty_list',
        'odd_items_num',
        'even_items_num'
    ]
)
def test__get_median_value__success(items, expected_result):
    assert get_median_value(items) == expected_result


@pytest.mark.xfail(reason='wrong implementation')
def test__get_median_value__order_invariance():
    items = [11, 9, 3, 5, 5]
    items_shuffled = [5, 11, 9, 3, 5]

    assert get_median_value(items) == get_median_value(items_shuffled)
