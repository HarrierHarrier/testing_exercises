import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize(
    'text,good_words,bad_words,expected_result',
    [
        ('Hello world', {'world'}, set(), 'GOOD'),
        ('Hello world', set(), {'world'}, 'BAD'),
        ('Hello world', {'hello'}, {'world'}, None),
        ('Hello world', {'Hello'}, set(), None),
        ('Hello world', set(), {'World'}, None)
    ],
    ids=[
        'good_tweet',
        'bad_tweet',
        'neutral_tweet',
        'good_words_case_sensitivity',
        'bad_words_case_sensitivity',
    ]
)
def test__check_tweet_sentiment__success(
    text, good_words, bad_words, expected_result
):
    assert check_tweet_sentiment(
        text, good_words, bad_words
    ) == expected_result
