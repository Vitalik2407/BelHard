# Написать функцию-генератор, принимающую 3 аргумента (number, start, end), все аргументы целочисленные.
# Генератор должен возвращать number в степени от start до end.

n = int(input('number='))
s = int(input('start='))
e = int(input('end='))


def step(number, start, end):
    while start <= end:
        a = number**start
        start += 1
        yield a


b = step(n, s, e)
result = []
for i in range(e - s + 1):
    result.append(next(b))
print(result)
