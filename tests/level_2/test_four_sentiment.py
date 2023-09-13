from functions.level_2.four_sentiment import check_tweet_sentiment


def test__check_tweet_sentiment__good_tweet():
    assert check_tweet_sentiment(
        'Hello world', set(['world']), set()
    ) == 'GOOD'


def test__check_tweet_sentiment__bad_tweet():
    assert check_tweet_sentiment(
        'Hello world', set(), set(['world'])
    ) == 'BAD'


def test__check_tweet_sentiment__neutral_tweet():
    assert check_tweet_sentiment(
        'Hello world', set(['hello']), set(['world'])
    ) is None
