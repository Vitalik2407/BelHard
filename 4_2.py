# Без использования collections, написать программу,
# которая будет создавать словарь для подсчитывания
# количества вхождений каждой буквы в текст введенный с клавиатуры.

text = input('Введите текст:')

list_text = list(text)

ftext = {list_text[i]: text.count(list_text[i]) for i in range(len(list_text))}
print(ftext)
print(list_text)
