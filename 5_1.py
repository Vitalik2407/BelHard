# Вывести первые N чисел кратные M и больше K

while not (N := input('введите число N:')).isdigit():
    pass
M = abs(int(input('введите число M:')))
K = int(input('введите число K:'))


# 1 способ
i = K
a = 1
while a <= int(N):
    i += 1
    if i % M:
        continue
    a += 1
    print(i)


# 2 способ
if K % M:
    a = 0
else:
    a = 1

for i in range(K + (M - K % M), K + (int(N) + a) * M, M):
    print(i)
