# Написать функцию перевода десятичного числа в двоичное и обратно,
# без использования функции int

def perevod(number_1):
    a = ""
    while number_1 > 0:
        b = str(number_1 % 2)
        a = b + a
        number_1 //= 2
    print(a)

    num = 1
    for i in range(len(a)-1):
        num = num * 2 + int(a[i+1])
    print(num)

perevod(number_1=int(input('введитеде десятичное число:')))


# def perevod_1(number):
#     a = bin(number)
#     print(a)
#
# n=int(input('введитеде десятичное число:'))
# perevod_1(n)
