# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

enter_text = input('Введите текст')
text = enter_text.split(' ')
text_new = '-'.join(text)
print(text_new)

# print(input('Введите текст').replace(' ', '-'))
