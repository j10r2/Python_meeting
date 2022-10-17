# n = int(input('введите натуральное число: '))
# dictionary = {}
# for i in range(1, n+1):
#     dictionary[i] = 3 * i + 1
# print(dictionary.items())

# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1

n = int(input('введите натуральное число: '))
dictionary = dict(enumerate(map(lambda i: 3*i+1, range(1, n+1)), start=1))
print(dictionary.items())