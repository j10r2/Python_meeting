# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

import random
list = []
for i in range (0, random.randint(10, 20)):
    list.append(random.randint(-10, 50))
unique_elements = []
for i in range (0, len(list)):
    if list[i] not in unique_elements:
        unique_elements.append(list[i])
print(list)
print(unique_elements)