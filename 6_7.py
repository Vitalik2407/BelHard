# Дан список чисел, необходимо для каждого элемента посчитать сумму его соседей,
# для крайних чисел одним из соседей является число с противоположной стороны списка

s = [1, 2, 3, 4, 5]


def sum_numb_2(a):
    b = a[len(a) - 1:] + a[0:len(a) - 1]
    c = a[1:] + a[0:1]
    d = list(map(sum, zip(b, c)))
    # print(b)
    # print(c)
    print(d)


sum_numb_2(s)


def sum_numb(b):
    c = []
    for i in range(len(b)):
        if i == 0:
            c.append(b[-1] + b[1])
        elif i == len(b)-1:
            c.append(b[len(b)-2] + b[0])
        else:
            c.append(b[i - 1] + b[i+1])
    print(c)


sum_numb(s)
