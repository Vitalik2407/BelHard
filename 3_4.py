# Пользователь вводит 3 числа. Сказать, сколько из них положительных и сколько отрицательных

first = float(input('Введите первое число'))
second = float(input('Введите второе число'))
third = float(input('Введите третье число'))

print(f'''Положительных чисел: {int(first >= 0) + int(second >= 0) + int(third >= 0)}
Отрицательных чисел: {int(first < 0) + int(second < 0) + int(third < 0)}''')
