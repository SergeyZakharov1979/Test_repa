# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def get_info(self):
#         return f'Название: {self.title}, Автор: {self.author}, Год: {self.year}'


# bk1 = Book('Война и Мир', 'Лев Толстой', '1975')
# print(bk1.get_info())


# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     def get_info(self):
#         return f"Имя: {self.name}, Оценка: {self.grade}"

# s1 = Student('Сергей Захаров', '5')
# print(s1.get_info())

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         if self.width > 0 and self.height > 0:
#             return self.width * self.height
#         else:
#             return 'Ошибка данных! Площадь не может быть отрицательной!'


# r1 = Rectangle(50, 40)
# print(r1.area())

# from math import pi


# class Circle:
#     """Класс для представления круга."""

#     def __init__(self, radius):
#         """Аргумент:
#         radius -- радиус круга (должен быть положительным)
#         """
#         self.radius = radius

#     def area(self):
#         """Вычисляет площадь прямоугольника.

#         Возвращает:
#         Площадь круга, если радиус положительный.
#         Генерирует ValueError, если радиус отрицательный.
#         """
#         if self.radius <= 0:
#             raise ValueError(
#                 "Ошибка данных! Площадь не может быть отрицательной!")
#         return pi * self.radius**2


# crl = Circle(60)
# print(crl.area())

# class BankAccount:
#     """Класс для имитации банковского кошелька"""

#     def __init__(self, balance: int):
#         """
#         Инициализация кошелька с заданным балансом.

#         Аргументы:
#             balance (number): баланс кошелька (должен быть положительным).
#         """
#         self.balance = balance

#     def deposit(self, amount: int):
#         """
#         Пополнение кошелька
#         Аргументы:
#             amount (number): средства пополнения кошелька (должен быть положительным)
#         """
#         self.balance += amount

#     def withdraw(self, amount: int):
#         """
#         Расход кошелька

#         Генерирует:
#             ValueError: Если расход больше баланса.
#         """
#         if self.balance < amount:
#             raise ValueError(
#                 "Ошибка данных! В вашем кошельке недостаточно средств!")
#         self.balance -= amount

#     def get_balance(self):
#         """
#         Возвращает баланс кошелька
#         """
#         return (self.balance)


# card = BankAccount(600000)
# print(card.get_balance())
# card.deposit(45000)
# print(card.get_balance())
# card.withdraw(9000)
# print(card.get_balance())
# card.withdraw(9000000)


class Transport():
    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year

    def get_info(self):
        print(self.brand, self.year)

    def move(self):
        return 'Транспорт движется'
    
tr = Transport("Honda", 2020)
tr.get_info()
print(tr.move())