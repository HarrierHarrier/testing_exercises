import pytest

from functions.level_1.three_url_builder import build_url


@pytest.mark.parametrize(
    ("host_name", "relative_url", "expected_result"),
    [
        ("https://github.com", "HarrierHarrier/testing_exercises", "https://github.com/HarrierHarrier/testing_exercises"),
        ("https://github.com", "", "https://github.com/"),
    ]
)
def test__build_url__check_default_params(
    host_name, relative_url, expected_result
):
    assert build_url(host_name, relative_url) == expected_result


@pytest.mark.parametrize(
    ("host_name", "relative_url", "get_params", "expected_result"),
    [
        ("https://github.com", "HarrierHarrier/testing_exercises", {"a": 1, "b": "2"}, "https://github.com/HarrierHarrier/testing_exercises?a=1&b=2"),
        ("https://github.com", "", {"foo": "spam", "hello": "world"}, "https://github.com/?foo=spam&hello=world"),
    ]
)
def test__build_url__check_custom_params(
    host_name, relative_url, get_params, expected_result
):
    assert build_url(host_name, relative_url, get_params) == expected_result
