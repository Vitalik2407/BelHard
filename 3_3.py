# Пользователь вводит Имя, Возраст и Город.
# Сформировать приветственное сообщение путем форматирования 3-мя способами

# 1 способ %-форматирование
name = input('Введите имя')
age = int(input('Введите возраст'))
town = input('Введите город')

if age % 10 == 1:
    nage = 'год.'
elif 1 < age % 10 < 5:
    nage = 'года.'
else:
    nage = 'лет.'

print('Привет! Меня зовут %s. \nМне %d %s \nЯ живу в городе %s.' % (name, age, nage, town))


# 2 способ format()
name = input('Введите имя')
age = int(input('Введите возраст'))
town = input('Введите город')

if age % 10 == 1:
    nage = 'год.'
elif 1 < age % 10 < 5:
    nage = 'года.'
else:
    nage = 'лет.'

print('Привет! Меня зовут {}. \nМне {} {} \nЯ живу в городе {}.'.format(name, age, nage, town))

# 3 способ f-строки
name = input('Введите имя')
age = int(input('Введите возраст'))
town = input('Введите город')

if age % 10 == 1:
    nage = 'год.'
elif 1 < age % 10 < 5:
    nage = 'года.'
else:
    nage = 'лет.'

print(f'Привет! Меня зовут {name}. \nМне {age} {nage} \nЯ живу в городе {town}.')
