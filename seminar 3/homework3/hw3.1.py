# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции
import random

list = []
summary = 0
for i in range (random.randint(6, 14)):
    list.append(random.randint(0, 15))
    if list[i] % 2 == 1:
        summary += list[i]
        print(list[i], end=' ')
print(list, '\n', summary)