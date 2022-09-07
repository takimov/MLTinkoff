import re
import random
from collections import defaultdict
import os


input_dir = input('Введите слово для начала текста, если такого нет, нажмите Enter: ')
if input_dir == '':
    with open(os.path.join('data', 'tolstoy.txt')) as f:
        text = f.read().lower()
else:
    input_dir = input_dir


def tokenize(text):
    return re.findall(r"[\w']+|[.,!?;]",  text)


corpus = tokenize(text)


def slicing(corpus, size):
    samples = (corpus[idx: idx + size] for idx, _ in enumerate(corpus))
    return [s for s in samples if len(s) == size]


def transitions(samples):
    transit = defaultdict(list)
    for sample in samples:
        first, second, third = sample
        transit[first].append(second)
    return transit


samples = slicing(corpus, size=3)
transits = transitions(samples)


def predict(chain, transit):
    last = chain[-1]
    nextie = transit[last]
    return random.choice(nextie) if nextie else ''


def generate_chain(start_text, transitions):
    chain = create_chain()

    while True:
        state = predict(chain, transitions)
        yield state
        chain.append(state)

def start():
    if input_dir == '':
        while True:
            start = random.choice(tokenize(text))
            if start not in ',./?!':
                break
        return start
    else:
        return input_dir


starting = start()
generator = generate_chain(starting, transits)


def create_chain():
    head = starting
    return tokenize(head)
