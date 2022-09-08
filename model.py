# -*- coding: utf-8 -*-
import os
from generate import result
from datetime import datetime

start_time = datetime.now()
with open('result.txt', 'w') as out:
    for i in result:
        out.write(i)

print('Результат генерации текста в файле result.txt и в консоли: ', os.path.abspath('result.txt'))
print('Путь к файлу model.py: ', os.path.abspath('model.py'))
