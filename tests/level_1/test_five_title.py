import pytest

from functions.level_1.five_title import change_copy_item


@pytest.mark.parametrize(
    "title",
    [
        "Item",
        "Name",
        "filename",
        "multiple words",
    ]
)
def test__change_copy_item__add_prefix(title):
    assert change_copy_item(title) == f"Copy of {title}"


@pytest.mark.parametrize(
    "title",
    [
        "Copy of Item",
        "Copy of Name",
        "Copy of filename",
        "Copy of multiple words",
    ]
)
def test__change_copy_item__add_copy_number(title):
    assert change_copy_item(title) == f"{title} (2)"


@pytest.mark.parametrize(
    "copy_num",
    [
        2,
        22,
        1234,
    ]
)
def test__change_copy_item__increase_copy_number(copy_num):
    assert change_copy_item(
        f"Copy of Item ({copy_num})"
    ) == f"Copy of Item ({copy_num + 1})"


def test__change_copy_item__check_max_length():
    assert change_copy_item("Item", 4) == "Item"
