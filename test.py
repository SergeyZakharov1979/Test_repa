from datetime import datetime


class Car:
    def __init__(self, brand, year, mileage, fuel):
        self.brand = brand
        self.year = year
        self.mileage = mileage
        self.fuel = fuel

    def show_info(self):
        if self.age() < 3:
            print(
                f'Машина {self.brand}, год выпуска {self.year}, пробег {self.mileage} километров.')
            print('🚗Новая машина!')
        elif self.age() > 10:
            print(
                f'Машина {self.brand}, год выпуска {self.year}, пробег {self.mileage} километров.')
            print('🔥Старая машина!')
        else:
            print(
                f'Машина {self.brand}, год выпуска {self.year}, пробег {self.mileage} километров.')

    def age(self):
        return datetime.now().year - self.year

    def drive(self, km):
        if km < 0:
            print('Нельзя проехать отрицательное расстояние!')
        elif (km / 100) * 7 > self.fuel:
            print(f'На вашу поездку не хватит топлива')
        else:
            self.mileage += km
            print(
                f'Проехали {km} километров. Израсходовано {(km / 100) * 7} литров топлива. Остаток в баке: {self.fuel - ((km / 100) * 7)} литров.')

    def refuel(self, liters):
        if liters < 0:
            print('Литры не могут быть отрицательные!')
        elif liters > 50:
            print('Невозможно заправить более 50 литров')
        else:
            self.fuel += liters
            return self.fuel


my_car = Car('Honda', 2023, 26000, 20)
my_car.show_info()
my_car.refuel(20)
my_car.drive(500)
my_car.show_info()
