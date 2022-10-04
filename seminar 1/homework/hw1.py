# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным

print('введите номер дня недели (от 1 до 7):')
while True:
    try:
        day = int(input())
        if day > 0 and day < 6:
            print('это не выходной день')
            break
        elif day == 6 or day == 7:
            print('збс, выходной')
            break
        else:
            print('инопланетянин, на Земле 7-дневная неделя')
    except:
        print('от 1 до 7 сказано')
