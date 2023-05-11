# Написать функцию-генератор, принимающую 3 аргумента (number, start, end), все аргументы целочисленные.
# Генератор должен возвращать number в степени от start до end.

n = int(input('number='))
s = int(input('start='))
e = int(input('end='))


def step(number, start, end):
    for i in range(start, end+1, 1):
        yield number**i


b = step(n, s, e)
result = []
for i in range(s, e+1, 1):
    result.append(next(b))
print(result)
