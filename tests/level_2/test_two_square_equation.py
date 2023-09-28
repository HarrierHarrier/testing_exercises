import pytest

from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize(
    "square_coefficient,linear_coefficient,const_coefficient,expected_result",
    [
        (1, 0, 1, (None, None)),
        (1, 0, 0, (0, 0)),
        (1, 1, 0, (-1, 0)),
        (0, 1, 0, (0, None)),
        (0, 0, 1, (None, None)),
    ],
    ids=[
        'no_roots',
        'one_root',
        'two_roots',
        'linear_equation',
        'invalid_linear_equation',
    ]
)
def test__solve_square_equation__success(
    square_coefficient, linear_coefficient, const_coefficient, expected_result
):
    assert solve_square_equation(
        square_coefficient, linear_coefficient, const_coefficient
    ) == expected_result
