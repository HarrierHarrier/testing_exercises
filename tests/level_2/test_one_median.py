import pytest

from functions.level_2.one_median import get_median_value


def test__get_median_value__empty_list():
    assert get_median_value([]) is None


# Тут parametrize помогает избежать того, что по случайности тест проходится
# как XPASS
@pytest.mark.xfail(reason="wrong implementation")
@pytest.mark.parametrize(
    "items,expected_result",
    [
        ([11, 9, 3, 5, 5], 5),
        ([1, 2, 3, 4, 5], 3),
    ]
)
def test__get_median_value__odd_items_num(items, expected_result):
    assert get_median_value(items) == expected_result


@pytest.mark.xfail(reason="wrong implementation")
@pytest.mark.parametrize(
    "items,expected_result",
    [
        ([1, 3, 5, 7], 4),
        ([1, 1, 2, 3], 1),
    ]
)
@pytest.mark.xfail(reason="wrong implementation")
def test__get_median_value__even_items_num(items, expected_result):
    assert get_median_value(items) == expected_result


@pytest.mark.xfail(reason="wrong implementation")
def test__get_median_value__order_invariance():
    items = [11, 9, 3, 5, 5]
    items_shuffled = [5, 11, 9, 3, 5]

    assert get_median_value(items) == get_median_value(items_shuffled)
