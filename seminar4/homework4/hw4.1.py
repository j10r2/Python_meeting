# Вычислить число π c заданной точностью d (10^{-1} ≤ d ≤10^{-10})
# при d = 0.001, π = 3.141
import math
d = 0
while True:
    d = int(input('с какой точностью вычисляем (введите число от 1 до 10)? '))
    if d > 0 and d <= 10:
        break
    print('некорректное число')
def t (number,digits):
    return ((number * 10**digits) // 1) / 10**digits
print(t (math.pi, d))