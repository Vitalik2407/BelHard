# Написать класс Car. Конструктор принимает атрибуты:
# color: str (цвет)
# count_passenger_seats: int (количество пассажирских мест)
# is_baby_seat: bool (наличие детского кресла)
# is_busy: bool (определяется внутри конструктора со значением False, не принимается на вход)
# Написать магический метод __str__ выводящий форматированную строку с информацией об автомобиле
class Car:

    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self) -> str:
        return f'''
         цвет : {self.color}, 
         кол-во мест : {self.count_passenger_seats}, 
         наличие детского кресла : {self.is_baby_seat}, 
         is busy : {self.is_busy}'''

    def __repr__(self) -> str:
        return f'''
         цвет = {self.color}, 
         кол-во мест = {self.count_passenger_seats}, 
         наличие детского кресла = {self.is_baby_seat}, 
         is busy = {self.is_busy}'''

car1 = Car('black', 5, True)
car2 = Car('blue', 6, False)
car3 = Car('red', 4, True)
car4 = Car('pink', 7, True)
car5 = Car('white', 7, False)
# print(car2.__str__())
cars = [car1, car2, car3, car4, car5]


# Написать класс Taxi. Конструктор принимает атрибуты:
# cars: list[Car] (cписок экземпляров класса Car)
# Реализовать метод find_car
# На вход метода поступают атрибуты: count_passenger_seats, is_baby (кол-во пассажиров, наличие ребенка,
# примечание: кол-во пассажиров с учетом ребенка, если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и свободный(is_busy = False),
# у автомобиля сменить атрибут is_busy на значение True, если подходящего авто нет, метод должен возвращать None


class Taxi:

    def __init__(self, cars: list) -> None:
        pass


    def find_car(self, count_passenger_seats, is_baby_seat) -> None:
        a = count_passenger_seats
        b = is_baby_seat
        for i in cars:
            if i.count_passenger_seats >= a and i.is_baby_seat == b and i.is_busy == False:
                i.is_busy = True
                return i
                break

print(Taxi.find_car(cars,  7, False))
