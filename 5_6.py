# "Угадай число"
# from random import randint
# a = randit(1, 100)
# Данная функция генерирует случайное число в заданном диапазоне,
# необходимо написать игру "угадай число" и сказать сколько попыток ушло
# на это у пользователя

from random import randint
a = randint(1, 100)
count_a = 1
print(a)
while not (N := int(input('Угадай число! Введите число N:')) == a):
    count_a += 1
    pass

print(f'Использовано попыток: {count_a}')
