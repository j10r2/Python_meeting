# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input('введите натуральное число: '))
a = number * 1
list = []
while number > 0:
    list.append(str(number%2))
    number //= 2
print(a, '=', end=' ')
for i in range (len(list)):
    print(list[-(i+1)], end='')