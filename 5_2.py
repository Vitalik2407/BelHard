# Сделать калькулятор: у пользователя спрашивается число,
# потом действие и второе число


try:
    number_1 = float(input('введите первое число:'))
except ValueError:
    number_1 = float(input('Это не число! Введите первое число:'))
except TypeError:
    number_1 = float(input('Неверный тип числа! Введите первое число:'))


action = input('введите действие (+, -, *, /):')

if action in ('+', '-', '*', '/'):

    try:
        number_2 = float(input('Введите второе число:'))
    except ValueError:
        number_2 = float(input('Это не число! Введите второе число:'))
    except TypeError:
        number_2 = float(input('Неверный тип числа! Введите второе число:'))

    if action == '+':
        print(f'{number_1 + number_2}')
    elif action == '-':
        print(f'{number_1 - number_2}')
    elif action == '*':
        print(f'{number_1 * number_2}')
    elif action == '/':
        if number_2 == 0:
            print('Делить на 0 нельзя!')
        else:
            print(f'{number_1 / number_2}')
else:
    action = input('Неверно указано действие! Введите действие (+, -, *, /):')
    try:
        number_2 = float(input('Введите второе число:'))
    except ValueError:
        number_2 = float(input('Это не число! Введите второе число:'))
    except TypeError:
        number_2 = float(input('Неверный тип числа! Введите второе число:'))

    if action == '+':
        print(f'{number_1 + number_2}')
    elif action == '-':
        print(f'{number_1 - number_2}')
    elif action == '*':
        print(f'{number_1 * number_2}')
    elif action == '/':
        if number_2 == 0:
            print('Делить на 0 нельзя!')
        else:
            print(f'{number_1 / number_2}')
