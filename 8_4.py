# 4. Изменить класс выше, список категорий должен содержать не просто имена категорий, а словари с данными о каждой
# категории (name: str, is_published: bool), а также изменить методы add, get, delete, update для работы со
# списком словарей.
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение ключа is_published на True.
# Если такого индекса нет, вызвать исключение IndexError.
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий значение ключа is_published на False.
# # Если такого индекса нет, вызвать исключение IndexError.

class Category:
    categories: list
    categories = []

    @classmethod
    def add(cls, name: str, is_published: bool):
        a = eval(f'{{"name": "{name}", "is_published": {is_published}}}')
        if a in cls.categories:
            raise ValueError('такая категория уже существует!')
        else:
            Category.categories.append(a)
            print(f'Индекс категории {a}: ', len(Category.categories) - 1)
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
    def update(cls, index, new_category, is_published):
        a = eval(f'{{"name": "{new_category}", "is_published": {is_published}}}')
        if a in cls.categories:
            raise ValueError('такая категория уже существует!')
        elif index > len(cls.categories)-1:
            cls.categories.append(a)
        else:
            cls.categories[index] = a

    @classmethod
    def make_published(cls, index):
        try:
            cls.categories[index]['is_published'] = True
        except IndexError:
            print('категория по данному индексу отсутствует!')

    @classmethod
    def make_unpublished(cls, index):
        try:
            cls.categories[index]['is_published'] = False
        except IndexError:
            print('категория по данному индексу отсутствует!')


Category.add('a1000', True)
Category.add('a2000', False)
Category.add('a3000', False)

print(Category.get(1))

Category.delete(1)

Category.update(5, 'a5000', False)

Category.make_published(1)

Category.make_unpublished(0)

print(Category.categories)
