from functions.level_2.two_square_equation import solve_square_equation


def test__solve_square_equation__no_roots():
    assert solve_square_equation(1, 0, 1) == (None, None)


def test__solve_square_equation__one_root():
    assert solve_square_equation(1, 0, 0) == (0, 0)


def test__solve_square_equation__two_roots():
    assert solve_square_equation(1, 1, 0) == (-1, 0)


def test__solve_square_equation__linear_equation():
    assert solve_square_equation(0, 1, 0) == (0, None)


def test__solve_square_equation__linear_incorrect_equation():
    assert solve_square_equation(0, 0, 1) == (None, None)
