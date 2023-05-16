# Написать класс Car. Конструктор принимает атрибуты:
# color: str (цвет)
# count_passenger_seats: int (количество пассажирских мест)
# is_baby_seat: bool (наличие детского кресла)
# is_busy: bool (определяется внутри конструктора со значением False, не принимается на вход)
# Написать магический метод __str__ выводящий форматированную строку с информацией об автомобиле
class Car:
    color: str
    count_passenger_seats: int
    is_baby_seat: bool

    def __init__(self, color, count_passenger_seats, is_baby_seat):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self) -> str:
        return f'''
         цвет = {self.color}, 
         кол-во мест = {self.count_passenger_seats}, 
         наличие детского кресла = {self.is_baby_seat}, 
         is busy = {self.is_busy}'''


car1 = Car('black', 5, True)
car2 = Car('blue', 6, False)
print(car2.__str__())
