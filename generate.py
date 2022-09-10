from train import transitions, tokenize, text, slicing, generate_chain, starting

#Собирает все функции из train, и создает generated_tokens,
# который создает список из элементов генератора generate_chain.
# Далее generated_tokens обрабатывается для того, чтобы пунктуация выглядела следующим видом:
# 'cлово'-'запятая'-'пробел'-'слово'
def generate(source, starting, words_count=input('Введите количество слов для генерации текста: ')):
    corpus = tokenize(source)
    samples = slicing(corpus, size=3)
    transits = transitions(samples)
    generator = generate_chain(starting, transits)
    generated_tokens = [next(generator) for _ in range(words_count)]
    if generated_tokens[0] in './,?!':
        del generated_tokens[0]
    for i in range(len(generated_tokens) - 1):
        if generated_tokens[i] in '/.,!?;:':
            generated_tokens[i] += ' '
        elif generated_tokens[i] and generated_tokens[i+1] not in '/.,!?;:':
            generated_tokens[i] += ' '
    return ''.join(generated_tokens).capitalize()


result = generate(source=text, starting=starting, words_count=100)
print(result)
