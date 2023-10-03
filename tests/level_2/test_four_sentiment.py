import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize(
    "text,good_words,bad_words",
    [
        ("Hello world", {"world"}, set()),
        (
            "Hello!, How do you do?, How d'ye do?, Good afternoon!,"
            " How are you?, Good man!",
            {"hello", "good"}, set()
        )
    ]
)
def test__check_tweet_sentiment__good_tweet(text, good_words, bad_words):
    assert check_tweet_sentiment(
        text, good_words, bad_words
    ) == "GOOD"


@pytest.mark.parametrize(
    "text,good_words,bad_words",
    [
        ("Hello world", set(), {"world"}),
        (
            "Hello!, How do you do?, How d'ye do?, Good afternoon!,"
            " How are you?, Good man!",
            set(), {"hello", "good"}
        )
    ]
)
def test__check_tweet_sentiment__bad_tweet(text, good_words, bad_words):
    assert check_tweet_sentiment(
        text, good_words, bad_words
    ) == "BAD"


@pytest.mark.parametrize(
    "text,good_words,bad_words",
    [
        ("Hello world", {"hello"}, {"world"}),
        (
            "Hello!, How do you do?, How d'ye do?, Good afternoon!,"
            " How are you?, Good man!",
            {"good"}, {"do?,"}
        )
    ]
)
def test__check_tweet_sentiment__neutral_tweet(text, good_words, bad_words):
    assert check_tweet_sentiment(
        text, good_words, bad_words
    ) is None


def test__check_tweet_sentiment__good_words_case_sensitivity():
    assert check_tweet_sentiment(
        "Hello world", {"Hello"}, set()
    ) is None


def test__check_tweet_sentiment__bad_words_case_sensitivity():
    assert check_tweet_sentiment(
        "Hello world", set(), {"World"}
    ) is None
