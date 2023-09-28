import pytest

from functions.level_1.three_url_builder import build_url


@pytest.mark.parametrize(
    "host_name,relative_url,get_params,expected_result",
    [
        ('https://github.com', 'HarrierHarrier/testing_exercises', None, 'https://github.com/HarrierHarrier/testing_exercises'),
        ('https://github.com', 'HarrierHarrier/testing_exercises', {'a': 1, 'b': '2'}, 'https://github.com/HarrierHarrier/testing_exercises?a=1&b=2'),
    ],
    ids=[
        'default_params',
        'custom_params',
    ]
)
def test__build_url__success(host_name, relative_url, get_params, expected_result):
    assert build_url(host_name, relative_url, get_params) == expected_result
