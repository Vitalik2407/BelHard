# Подсчитать среднее арифметическое N чисел, вводимых с клавиатуры
N = input('Введите числа через пробел или запятую:')
M = (N.replace(' ', ',')).split(',')

numb = 0
for i in range(len(M)):
    numb += int(M[i])

numb_1 = numb / len(M)
print(numb_1)
