# Написать рекурсивную функцию, принимающую строку и разворачивающую ее задом на перед


def rec(a):
    if len(a) == 1:
        b = a[0]
        return b
    else:
        b = a[len(a) - 1] + rec(a[0:len(a) - 1])
    return b


c = 'hello'
print(rec(c))
