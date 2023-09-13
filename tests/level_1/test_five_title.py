from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    # Проверки
    assert change_copy_item('Item') == 'Copy of Item'
    assert change_copy_item('Item', 4) == 'Item'
    assert change_copy_item('Copy of Item') == 'Copy of Item (2)'
    assert change_copy_item('Copy of Item (2)') == 'Copy of Item (3)'
