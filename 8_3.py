# Реализовать класс Category.
# Создать атрибут класса categories.
# 3.1 Написать метод класса add принимающий на вход название категории,
# если такой категории в атрибуте класса categories нет, добавить данную категорию в список
# и вернуть индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать исключение ValueError.
# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка категорий на этом индексе,
# если нет элемента на таком индексе, вызвать исключение IndexError.
# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и удаляющий элемент из списка
# категорий на этом индексе, если нет элемента на таком индексе, ничего не делать, метод ничего возвращать не должен.
# 3.4 Написать метод класса update принимающий индекс категорий и новое название категории,
# если нет элемента на таком индексе, то новая категория должна добавляться с учетом того, что имена категорий
# уникальны, если новое имя категории нарушает уникальность в списке категорий, вызвать исключение ValueError.

class Category:
    categories: list
    categories = []

    @classmethod
    def add(cls, category_name):
        if category_name in Category.categories:
            raise ValueError('такая категория уже существует!')
        else:
            Category.categories.append(category_name)
            print(f'Индекс категории {category_name}: ', len(Category.categories) - 1)
        return len(Category.categories)-1

    @classmethod
    def get(cls, index):
        try:
            return cls.categories[index]
        except IndexError:
            print('категория по данному индексу отсутствует!')

    @classmethod
    def delete(cls, index):
        try:
            cls.categories.pop(index)
        except IndexError:
            ''

    @classmethod
    def update(cls, index, new_category):
        if new_category in cls.categories:
            raise ValueError('такая категория уже существует!')
        elif index > len(cls.categories)-1:
            cls.categories.append(new_category)
        else:
            cls.categories[index] = new_category


Category.add('a1000')
Category.add('a2000')
Category.add('a3000')

print(Category.get(1))

Category.delete(1)

Category.update(5, 'a5000')

print(Category.categories)
