import re
import random
from collections import defaultdict
import os

list_files = dict()
for files in os.listdir('data'):
    list_files.update({os.listdir('data').index(files): files})


for i in list_files:
    print(i, ' - ', list_files[i])


file = int(input('Выберите файл для генерации(укажите порядковый номер): '))


with open(os.path.join('data', list_files[file])) as f:
    text = f.read().lower()


input_dir = input('Введите слово для начала текста, если такого нет, нажмите Enter: ')

#Возвращает исходный текст в виде списка, разбитого на слова и пунктуацию, как отдельные элементы.
def tokenize(text):
    return re.findall(r"[\w']+|[.,!?;]",  text)


corpus = tokenize(text)

#Разбивает на подсписки длиной size, состоящие из элементов tokenize(text).
def slicing(corpus, size):
    samples = (corpus[idx: idx + size] for idx, _ in enumerate(corpus))
    return [s for s in samples if len(s) == size]

#Создает defaultdict с классом list,
# состоящий из ключей - слов текста; значений - всех слов, стоящих после этого слова(ключа) в тексте.
def transitions(samples):
    transit = defaultdict(list)
    for sample in samples:
        first, second, third = sample
        transit[first].append(second)
    return transit


samples = slicing(corpus, size=3)
transits = transitions(samples)

#Создает цепь, в которой берется последнее слово цепи,
# а за ним "наугад" создается следующее слово из списка слов, вызванных transit[last].
def predict(chain, transit):
    last = chain[-1]
    nextie = transit[last]
    return random.choice(nextie) if nextie else ''

#Возвращает input_dir, как стартовое слово, если оно было введено,
# если нет, то выбирает "наугад" элемент из списка, если элемент не является знаком препинания.
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

#Генерация готовой цепи.(Функция генератор)
def generate_chain(start_text, transitions):
    chain = [start_text]
    counter = 0
    while True:
        if counter != 0:
            state = predict(chain, transitions)
            yield state
            chain.append(state)
        else:
            counter += 1
            yield chain[0]
            chain.append(start_text)


generator = generate_chain(starting, transits)
