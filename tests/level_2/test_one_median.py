import pytest

from functions.level_2.one_median import get_median_value


def test__get_median_value__empty_list():
    assert get_median_value([]) is None


@pytest.mark.xfail(reason='wrong implementation')
def test__get_median_value__odd_items_num():
    assert get_median_value([11, 9, 3, 5, 5]) == 5


@pytest.mark.xfail(reason='wrong implementation')
def test__get_median_value__order_invariance():
    items = [11, 9, 3, 5, 5]
    items_shuffled = [5, 11, 9, 3, 5]

    assert get_median_value(items) == get_median_value(items_shuffled)


@pytest.mark.xfail(reason='wrong implementation')
def test__get_median_value__even_items_num():
    assert get_median_value([1, 3, 5, 7]) == 4
