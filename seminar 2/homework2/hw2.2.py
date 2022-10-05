n = int(input('введите натуральное число: '))
list = [1]
for i in range (1, n):
    list.append(list[i-1]*(i+1))
print(list)