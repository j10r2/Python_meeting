import random

import hw4_4 as pr
import pe_method as pe
import list_sum as ls

pr.polinomal_write('polinomal_1.md', random.randint(3, 10)) # записываем во вспомогательном файле случайное уравнение
pr.polinomal_write('polinomal_2.md', random.randint(4, 8))
pol1 = open('polinomal_1.md').read() # извлекаем текст
pol2 = open('polinomal_2.md').read()
print(pol1, '\n', pol2)

list_1 = [[],[]]
list_2 = [[],[]]
pe.polinomal_extraction(pol1, list_1) # расшифровываем текст и переводим коэффициенты и степени в двумерный массив
pe.polinomal_extraction(pol2, list_2)
print(list_1)
print(list_2)
if list_1[0][0] > list_2[0][0]: # определяем, в каком массиве максимальная степень
    max_list = list_1
    min_list = list_2
else:
    max_list = list_2
    min_list = list_1
list1 = ls.list_summary(max_list, min_list) # сравниваем массивы и суммируем/вносим по порядку значения из одного в другой
# это очень тяжко было (-ж-)
print(list1)
with open('hw4.5.md', 'w') as data:
    count = 0
    for i in range(len(list1[0])):
        if list1[1][i] != 0 and list1[0][i] > 1:
            if count > 0 and list1[0][i] > 0:
                data.write('+')
            data.write(f'{list1[1][i]}x<sup>{list1[0][i]}</sup>')
            count +=1
        elif list1[1][i] != 0 and list1[0][i] == 1:
            if count > 0 and list1[1][i] > 0:
                data.write('+')
            data.write(f'{list1[1][i]}x')
            count +=1
        elif list1[1][i] != 0 and list1[0][i] == 0:
            if count > 0 and list1[1][i] > 0:
                data.write('+')
            data.write(f'{list1[1][i]}')
            count +=1
    data.write(f' = 0')
