from functions.level_1.three_url_builder import build_url


def test__build_url__check_default_params():
    assert build_url(
        host_name='https://github.com',
        relative_url='HarrierHarrier/testing_exercises'
    ) == 'https://github.com/HarrierHarrier/testing_exercises'


def test__build_url__check_custom_params():
    assert build_url(
        host_name='https://github.com',
        relative_url='HarrierHarrier/testing_exercises',
        get_params={'a': 1, 'b': '2'}
    ) == 'https://github.com/HarrierHarrier/testing_exercises?a=1&b=2'
