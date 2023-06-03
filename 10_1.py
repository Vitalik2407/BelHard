# Написать произвольную простую (без вложенностей) схему Pydatic.
# 1.Написать класс метод from_csv принимающий объект file (csv) и возвращающий список экземпляров схемы
# заполненных на основании этого файла.
# 2.Написать метод объекта to_csv принимающий объект файла (csv) и дописывающий/записывающий информацию из схемы
# в этот csv файл.


# from pydantic import BaseModel
# import csv
#
#
# class CSV(BaseModel):
#     first_name: str
#     second_name: str
#     age: int
#
#     def __init__(self, first_name, second_name, age):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.age = age
#
#     def __repr__(self) -> dict:
#         a = {'first_name': self.first_name, 'second_name': self.second_name, 'age': self.age}
#         return a
#
#     @classmethod
#     def from_csv(cls, text):
#         with open(str(text), 'r', encoding='utf-8') as file:
#             a = []
#             r = csv.reader(file)
#             for line in r:
#                 a.append(list(line))
#             # print(a)
#             b = []
#             for i in a[1:]:
#                 z = CSV(i[0], i[1], i[2])
#                 b.append(CSV.__repr__(z))
#             return b
#
#     def to_csv(self, text, first_name, second_name, age):
#         with open(str(text), 'a+', encoding='utf-8', newline='') as file:
#             r = csv.writer(file)
#             r.writerow([str(first_name), str(second_name), int(age)])
#
#
# csv_file = CSV.from_csv('Pydantic.csv')
# print(csv_file)
# CSV.to_csv(csv_file, 'Pydantic.csv', 'grisha', 'ivanov', '29')
#
# first_name,second_name,age
# ivan,hot,25
# leva,mirniy,32
# sveta,kot,28

from pydantic import BaseModel
import csv


class CSV(BaseModel):
    first_name: str
    second_name: str
    age: int

    def __init__(self, first_name, second_name, age) -> None:
        super().__init__(first_name=first_name, second_name=second_name, age=age)
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def __repr__(self) -> dict:
        a = {'first_name': self.first_name, 'second_name': self.second_name, 'age': self.age}
        return a

    @classmethod
    def from_csv(cls, text) -> list:
        with open(str(text), 'r', encoding='utf-8') as file:
            a = []
            r = csv.reader(file)
            for line in r:
                a.append(list(line))
            # print(a)
            b = []
            for i in a[1:]:
                z = CSV(i[0], i[1], i[2])
                b.append(CSV.__repr__(z))
            return b

    def to_csv(self, text, first_name, second_name, age):
        with open(str(text), 'a+', encoding='utf-8', newline='') as file:
            r = csv.writer(file)
            r.writerow([str(first_name), str(second_name), int(age)])


csv_file = CSV.from_csv('Pydantic.csv')
print(csv_file)
CSV.to_csv(csv_file, 'Pydantic.csv', 'grisha', 'ivanov', '29')

# first_name,second_name,age
# ivan,hot,25
# leva,mirniy,32
# sveta,kot,28
