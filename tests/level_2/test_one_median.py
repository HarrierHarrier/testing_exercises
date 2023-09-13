# Вопрос: тестируемая функция должна правильно работать и проходить тесты или
# мы пишем правильные тесты и функция намеренно их не проходит?  Смущает, что
# только это задание выглядит подозрительно.
#
# Проблемы с функцией, на мой взгляд, такие:
# 1. middle_index считается неправильно из-за чего можно словить IndexError
#   или неправильное значение
# 2. В ретурнах мы обращаемся к неотсортированному списку (items вместо
#   sorted_items), так мы медиану не посчитаем
# 3. В случае четного количества элементов (второй ретурн) должна возвращаться
#   полусумма срединных элементов, т.е. нужно использовать обычное деление,
#   а не целочисленное
# 4. Аннотация типа возвращаемого значения - в случае с чётным количеством
#   элементов может возвращаться float


from functions.level_2.one_median import get_median_value


def test__get_median_value__empty_list():
    assert get_median_value([]) is None


def test__get_median_value__odd_items_num():
    assert get_median_value([11, 9, 3, 5, 5]) == 5


def test__get_median_value__order_invariance():
    items = [11, 9, 3, 5, 5]
    items_shuffled = [5, 11, 9, 3, 5]

    assert get_median_value(items) == get_median_value(items_shuffled)


def test__get_median_value__even_items_num():
    assert get_median_value([1, 3, 5, 7]) == 4


def test__get_median_value__even_items_num_float():
    assert get_median_value([1, 4, 3, 2]) == 2.5
