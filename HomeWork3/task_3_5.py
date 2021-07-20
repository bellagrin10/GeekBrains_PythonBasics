from random import choice, choices, sample


def get_jokes(n, *args, flag=False, **kwargs):
    """
    The function returns n jokes formed from three random words taken from three lists (one from each):
    arguments can be positional or named
    :param n: int - the required number of jokes
    :param args: lists with words
    :param flag: allows (True) or prohibits (False) repetitions of words in jokes
    :param kwargs: named lists with words
    :return: list of formed jokes
    """
    jokes_data = None
    if args:
        jokes_data = args
    elif kwargs:
        jokes_data = kwargs.values()
    if flag:
        joke_formed = [' '.join(map(choice, jokes_data)) for _ in range(n)]
        # the same using choices:
        # words_to_form_jokes = (choices(i, k=n) for i in jokes_data)
        # joke_formed = [' '.join(joke_words) for joke_words in zip(*words_to_form_jokes)]
    else:
        words_to_form_jokes = (sample(i, k=n) for i in jokes_data)
        joke_formed = [' '.join(joke_words) for joke_words in zip(*words_to_form_jokes)]
    return joke_formed


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(4, nouns, adverbs, adjectives))
print(get_jokes(3, nouns, adverbs, adjectives, flag=True))
print(get_jokes(4, n_=nouns, adv_=adverbs, adj_=adjectives))
print(get_jokes(3, flag=True, n_=nouns, adv_=adverbs, adj_=adjectives))
