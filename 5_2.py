# Сделать калькулятор: у пользователя спрашивается число,
# потом действие и второе число

number_1 = input('введите первое число:')
try:
    float(number_1)
except ValueError:
    number_1 = input('Это не число! Введите первое число:')
except TypeError:
    number_1 = input('Неверный тип числа! Введите первое число:')
number_1 = float(number_1)

action = input('введите действие (+, -, *, /):')

if action in ('+', '-', '*', '/'):
    number_2 = input('введите второе число:')

    try:
        float(number_2)
    except ValueError:
        number_2 = input('Это не число! Введите второе число:')
    except TypeError:
        number_2 = input('Неверный тип числа! Введите второе число:')
    number_2 = float(number_2)
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
    number_2 = input('введите второе число:')

    try:
        float(number_2)
    except ValueError:
        number_2 = input('Это не число! Введите второе число:')
    except TypeError:
        number_2 = input('Неверный тип числа! Введите второе число:')
    number_2 = float(number_2)
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
