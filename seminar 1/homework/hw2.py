print('введите координаты точки, не равные 0:')
x = None
y = None
while True:
    try:
        print('X: ', end = '')
        x = float(input())
        print('Y: ', end = '')
        y = float(input())
        if x != 0 and y != 0:
            break
        else:
            print('не равные 0')
    except:
        print('читаем внимательно:')
if x > 0 and y > 0:
    quarter = 'I'
elif x < 0 and y > 0:
    quarter = 'II'
elif x < 0 and y < 0:
    quarter = 'III'
else:
    quarter = 'IV'
print(f'точка с координатами ({x}, {y}) принадлежит {quarter}-й четверти')