# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random

list = []
for i in range (random.randint(6, 15)):
    list.append(round(random.random(), 2))

modulo_min = list[0] % 1
modulo_max = list[0] % 1
for i in list:
    if i % 1 < modulo_min:
        modulo_min = i % 1
        print('min=', i % 1, end=" ")
    elif i % 1 > modulo_max:
        modulo_max = i % 1
        print('max=', i % 1, end=" ")
        
print(list, '\n', modulo_max - modulo_min)