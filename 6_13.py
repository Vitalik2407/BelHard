# Написать рекурсивную функцию, которая принимает целое число (depth), функция должна генерировать дерево
# указанной глубины (каждая ветвь имеет 2 дочерних ветки): depth=3, result=[[[],[]],[[],[]]].

def rec(depth):
    if depth == 1:
        result = '[]'
        return result
    else:
        result = '[' + rec(depth - 1) + ',' + rec(depth - 1) + ']'
    return result


print(rec(int(input('ведите целое положительное число:'))))
