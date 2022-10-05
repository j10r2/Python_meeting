n = int(input('введите натуральное число: '))
dictionary = {}
for i in range(n+1):
    dictionary[i] = 3 * i + 1
print(dictionary.items())