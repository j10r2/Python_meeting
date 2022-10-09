# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

number = int(input('введите число: '))
def multiplier_list (a):
    simple_multiplier_list = [2, 3, 5, 7]
    for i in range (10, a+1):
        if i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 !=0:
            simple_multiplier_list.append(i)
    result_list = []
    while a != 1:
        for i in range(len(simple_multiplier_list)):
            if a % simple_multiplier_list[i] == 0:
                result_list.append(simple_multiplier_list[i])
                break
        a //= simple_multiplier_list[i]
    return result_list
print(f'список простых множителей числа {number}: ', multiplier_list(number))