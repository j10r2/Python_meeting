# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции
import random
summary = 0
list1 = list(map(lambda i: random.randint(0,15), range (random.randint(6, 14))))
for i in range (len(list1)):
    if i % 2 == 1:
        summary += list1[i]
print(summary)