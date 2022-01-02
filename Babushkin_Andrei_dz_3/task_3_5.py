def get_jokes(n, flag):

    """Данная функция генерирует случайные шутки. Аргумент флаг разрешает/запрещает повотры слов в шутках"""
    import random
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    if flag == False:
        random.shuffle(nouns)
        random.shuffle(adverbs)
        random.shuffle(adjectives)
        for noun, adverb, adjective in zip(nouns, adverbs, adjectives):
            jokes.append(f'{noun} {adverb} {adjective}')
    elif flag == True:
        while n:
            noun = random.choice(nouns)
            adverb = random.choice(adverbs)
            adjective = random.choice(adjectives)
            jokes.append(f'{noun} {adverb} {adjective}')
            n -= 1
        return jokes

    return jokes[:n]


print(get_jokes(flag=True, n=6))