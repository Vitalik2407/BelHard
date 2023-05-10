# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение - словарь с данными пользователя
# (имя, фамилия, телефон, почта), вывести имена тех, у кого не указана почта(нет ключа email или значение этого ключа -
# пустая строка)

f = {'1': {'name': 'Vanya', 'second name': 'Smirnof', 'telephone': '+375295555555', 'email': 'vs@mail.ru'},
     '2': {'name': 'Petr', 'second name': 'Sidorof', 'telephone': '+375297777777'},
     '3': {'name': 'Vano', 'second name': 'Smit', 'telephone': '+375294444444', 'email': ''},
     '4': {'name': 'Varya', 'second name': 'Snof', 'telephone': '+375293333333', 'email': 'pt@mail.ru'},
     '5': {'name': 'Vlad', 'second name': 'Smidt', 'telephone': '+375292222222', 'email': ''},
     }


def search(a):
     for i, j in a.items():
          if j.get('email') == '' or j.get('email') == None:
               print(j.get('name'))


search(f)
