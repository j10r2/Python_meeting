# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

list = []
for i in range (random.randint(6, 14)):
    list.append(random.randint(0, 15))

new_list = []
for i in range (len(list)//2):
    new_list.append(list[i] * list[-(i+1)])

print(list, '\n', new_list)