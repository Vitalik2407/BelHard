# Дан список чисел и на вход поступает число N, необходимо сместить список на указанное число

spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def sdvig(n):
    print(spisok[len(spisok)-n:] + spisok[0:len(spisok)-n])


N = int(input('введите число N:'))

sdvig(N)
