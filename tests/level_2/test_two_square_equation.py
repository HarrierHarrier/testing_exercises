import pytest

from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize(
    "square_coefficient,linear_coefficient,const_coefficient",
    [
        (1, 0, 1),
        (5, -2, 9),
        (-10, 4, -10),
        (6, 1, 4),
        (-4, 10, -10),
        (10, -5, 8)
    ]
)
def test__solve_square_equation__no_roots(
    square_coefficient, linear_coefficient, const_coefficient
):
    assert solve_square_equation(
        square_coefficient, linear_coefficient, const_coefficient
    ) == (None, None)


@pytest.mark.parametrize(
    "square_coefficient,linear_coefficient,const_coefficient,expected_result",
    [
        (1, 0, 0, 0.0),
        (4, 8, 4, -1.0),
        (-1, 4, -4, 2.0),
        (-8, 8, -2, 0.5),
        (-4, 4, -1, 0.5),
        (2, 8, 8, -2.0),
    ]
)
def test__solve_square_equation__one_root(
    square_coefficient, linear_coefficient, const_coefficient,
    expected_result: float
):
    assert solve_square_equation(
        square_coefficient, linear_coefficient, const_coefficient
    ) == (expected_result, expected_result)


@pytest.mark.parametrize(
    "square_coefficient,linear_coefficient,const_coefficient,expected_result",
    [
        (1, 1, 0, (-1.0, 0.0)),
        (1, 27, 26, (-26.0, -1.0)),
        (-6, -42, -72, (-3.0, -4.0)),
        (-3, 42, 96, (16.0, -2.0)),
        (14, -84, 70, (1.0, 5.0)),
        (19, 57, 0, (-3.0, 0.0)),
    ]
)
def test__solve_square_equation__two_roots(
    square_coefficient, linear_coefficient, const_coefficient,
    expected_result: tuple[float, float]
):
    assert solve_square_equation(
        square_coefficient, linear_coefficient, const_coefficient
    ) == expected_result


@pytest.mark.parametrize(
    "linear_coefficient,const_coefficient,expected_result",
    [
        (1, 0, 0),
        (-20, -92, -4.6),
        (24, -45, 1.875),
        (-24, -9, -0.375),
        (4, 50, -12.5),
        (22, -66, 3.0),
    ]
)
def test__solve_square_equation__linear_equation(
    linear_coefficient, const_coefficient, expected_result: float
):
    assert solve_square_equation(
        0, linear_coefficient, const_coefficient
    ) == (expected_result, None)


@pytest.mark.parametrize(
    "const_coefficient",
    [
        1,
        -15,
        82,
        84,
        85,
    ]
)
def test__solve_square_equation__linear_incorrect_equation(const_coefficient):
    assert solve_square_equation(0, 0, const_coefficient) == (None, None)
