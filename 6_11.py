# Написать функцию-генератор, принимающую целое число count и возвращающую указанное количество простых чисел

c = int(input('введите положительное целое число:'))


def numb(a):
    if not a % 2:
        return False

    for i in range(2, a//2 + 1):
        if not a % i:
            return False

    return True


def generator(count):
    count -= 1
    yield 2
    a = 3
    while count:
        if numb(a):
            count -= 1
            yield a
        a += 2


print(*generator(c))
