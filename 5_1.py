# Вывести первые N чисел кратные M и больше K
N = int(input('введите число N:'))
M = int(input('введите число M:'))
K = int(input('введите число K:'))

# 1 способ
i = K
a = 1
while a <= N:
    i += 1
    if i % M:
        continue
    a += 1
    print(i)

# 2 способ
for i in range(K + (M - K % M), K + (N + 1) * M, M):
    print(i)
