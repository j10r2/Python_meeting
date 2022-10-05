import random
list = []
for i in range (0, random.randint(10, 20)):
    list.append(random.randint(-10, 50))
print(list)
for i in range (0, len(list) - 1):
    j = random.randint(0, len(list) - 1)
    list[i], list[j] = list[j], list[i]
print(list)