import pytest

from functions.level_1.five_title import change_copy_item


@pytest.mark.parametrize(
    'title,max_main_item_title_length,expected_result',
    [
        ('Item', 100, 'Copy of Item'),
        ('Copy of Item', 100, 'Copy of Item (2)'),
        ('Copy of Item (2)', 100, 'Copy of Item (3)'),
        ('Item', 4, 'Item'),
    ],
    ids=[
        'add_prefix',
        'add_copy_number',
        'increase_copy_number',
        'exceed_max_length',
    ]
)
def test__change_copy_item__success(title, max_main_item_title_length, expected_result):
    assert change_copy_item(title, max_main_item_title_length) == expected_result
