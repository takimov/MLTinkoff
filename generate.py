from train import transitions, tokenize, text, slicing, generate_chain, starting



def generate(source, start=starting, words_count=input('Введите количество слов для генерации текста: ')):
    corpus = tokenize(source)
    samples = slicing(corpus, size=3)
    transits = transitions(samples)

    generator = generate_chain(start, transits)
    generated_tokens = [next(generator) for _ in range(words_count)]
    if generated_tokens[0] in './,?!':
        del generated_tokens[0]
    for i in range(len(generated_tokens) - 1):
        if generated_tokens[i] in '/.,!?;:':
            generated_tokens[i] += ' '
        elif generated_tokens[i] and generated_tokens[i+1] not in '/.,!?;:':
            generated_tokens[i] += ' '

    return ''.join(generated_tokens).capitalize()


result = generate(source=text, words_count=100)
print(result)
