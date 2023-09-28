from functions.level_2.four_sentiment import check_tweet_sentiment


def test__check_tweet_sentiment__good_tweet():
    assert check_tweet_sentiment(
        'Hello world', {'world'}, set()
    ) == 'GOOD'


def test__check_tweet_sentiment__bad_tweet():
    assert check_tweet_sentiment(
        'Hello world', set(), {'world'}
    ) == 'BAD'


def test__check_tweet_sentiment__neutral_tweet():
    assert check_tweet_sentiment(
        'Hello world', {'hello'}, {'world'}
    ) is None


def test__check_tweet_sentiment__good_words_case_sensitivity():
    assert check_tweet_sentiment(
        'Hello world', {'Hello'}, set()
    ) is None


def test__check_tweet_sentiment__bad_words_case_sensitivity():
    assert check_tweet_sentiment(
        'Hello world', set(), {'World'}
    ) is None
