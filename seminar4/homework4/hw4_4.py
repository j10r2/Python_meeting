# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random

degree = random.randint(4, 8)
file = 'hw4.4.md'
def polinomal_write (file, degree):
    with open(file, 'w') as data:
        count = 0
        while degree >= 0:
            k = random.randint(-5, 4)
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