# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random

degree = int(input('введите степень многочлена: '))
with open('hw4.4.md', 'w') as data:
    count = 0
    while degree >= 0:
        k = random.randint(-10, 10)
        if k != 0 and degree > 1:
            if count > 0 and k > 0:
                data.write('+')
            data.write(f'{k}x<sup>{degree}</sup>')
            count +=1
        elif k != 0 and degree == 1:
            if count > 0 and k > 0:
                data.write('+')
            data.write(f'{k}x')
            count +=1
        elif k != 0 and degree == 0:
            if count > 0 and k > 0:
                data.write('+')
            data.write(f'{k}')
            count +=1
        degree -=1
    data.write(f' = 0')