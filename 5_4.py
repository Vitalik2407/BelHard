# Вводится число, найти его максимальную цифру
N = int(input('Введите целое число'))
M = list(str(N))
numb = M[0]
for i in range(len(M)):
    if M[i] > numb:
        numb = M[i]
print(numb)
