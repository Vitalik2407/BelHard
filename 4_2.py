# Без использования collections, написать программу,
# которая будет создавать словарь для подсчитывания
# количества вхождений каждой буквы в текст введенный с клавиатуры.
text = input('Введите текст:')

mn_text = set(text)
list_text = list(mn_text)

ftext = {list_text[i]: text.count(list_text[i]) for i in range(len(list_text))}
print(ftext)
