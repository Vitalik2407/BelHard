# Заполнить список степенями числа 2 (от 2^1 до 2^n).

count_n = int(input('Введите целое положительное число n'))

list_2n = [2**i for i in range(1, count_n+1)]
print(list_2n)
