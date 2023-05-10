# Дан словарь, ключ - Название страны, значение - список городов,
# на вход поступает город, необходимо сказать из какой он страны

s = {'Belarus': 'Minsk, Grodno, Gomel',
     'Poland': 'Bialostok, Warszawa',
     'Russia': 'Moskow, Tver, Smolensk'}

a = input('введите город:')


def country(value):
    for i, j in s.items():
        if value in j:
            print(i)


country(a)
