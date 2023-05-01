# Вывести четные числа от 2 до N по 5 в строку

try:
    N = int(input('введите целое число N:'))
except ValueError:
    N = int(input('Это не число! Введите целое число N:'))

if N > 2:
    b = 1
else:
    b = -1
a = 0
for i in range(2, N + b, 2):
    a += 1
    if a % 5 > 0:
        print(i, end=', ')
    else:
        print(i, end='\n')
