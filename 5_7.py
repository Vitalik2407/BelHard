# В мире ведьмака существуют монеты номиналом: 1, 5, 10, 25.
# Необходимо введенную сумму разбить на минимальное количество монет:

cash = int(input('Сумма к оплате:'))

coin_25 = cash//25
coin_10 = (cash-coin_25*25)//10
coin_5 = (cash-coin_25*25-coin_10*10)//5
coin_1 = (cash-coin_25*25-coin_10*10-coin_5*5)

print(f'К оплате будет:\nмонет по 25: {coin_25}шт.,\nмонет по 25: {coin_10}шт.,'
      f'\nмонет по 5: {coin_5}шт.,\nмонет по 1: {coin_1}шт..')
