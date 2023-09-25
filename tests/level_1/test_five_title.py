from functions.level_1.five_title import change_copy_item


def test__change_copy_item__add_prefix():
    assert change_copy_item('Item') == 'Copy of Item'


def test__change_copy_item__add_copy_number():
    assert change_copy_item('Copy of Item') == 'Copy of Item (2)'


def test__change_copy_item__increase_copy_number():
    assert change_copy_item('Copy of Item (2)') == 'Copy of Item (3)'


def test__change_copy_item__check_max_length():
    assert change_copy_item('Item', 4) == 'Item'
