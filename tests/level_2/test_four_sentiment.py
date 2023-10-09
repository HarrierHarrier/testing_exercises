import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize(
    "text",
    [
        "Good day",
        "Excellent idea",
        "This is awesome"
    ]
)
def test__check_tweet_sentiment__good_tweet(text):
    good_words = {
        "good", "excellent", "awesome"
    }
    bad_words = {
        "bad", "repulsive", "terrible"
    }

    assert check_tweet_sentiment(
        text, good_words, bad_words
    ) == "GOOD"


@pytest.mark.parametrize(
    "text",
    [
        "I have a bad feeling about this",
        "I find this repulsive",
        "What a terrible idea"
    ]
)
def test__check_tweet_sentiment__bad_tweet(text):
    good_words = {
        "good", "excellent", "awesome"
    }
    bad_words = {
        "bad", "repulsive", "terrible"
    }

    assert check_tweet_sentiment(
        text, good_words, bad_words
    ) == "BAD"


@pytest.mark.parametrize(
    "text",
    [
        "I don`t think it is bad , it`s good",
        "You think this is excellent , but I find this repulsive",
        "Ivan the Terrible had an awesome hat"
    ]
)
def test__check_tweet_sentiment__neutral_tweet(text):
    good_words = {
        "good", "excellent", "awesome"
    }
    bad_words = {
        "bad", "repulsive", "terrible"
    }

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
