from datetime import datetime
from math import pi


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f'Название: {self.title}, Автор: {self.author}, Год: {self.year}'


bk1 = Book('Война и Мир', 'Лев Толстой', '1975')
print(bk1.get_info())


# ****************************************************

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_info(self):
        return f"Имя: {self.name}, Оценка: {self.grade}"


s1 = Student('Сергей Захаров', '5')
print(s1.get_info())

# ****************************************************


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        if self.width > 0 and self.height > 0:
            return self.width * self.height
        else:
            return 'Ошибка данных! Площадь не может быть отрицательной!'


r1 = Rectangle(50, 40)
print(r1.area())

# ****************************************************


class Circle:
    """Класс для представления круга."""

    def __init__(self, radius):
        """Аргумент:
        radius -- радиус круга (должен быть положительным)
        """
        self.radius = radius

    def area(self):
        """Вычисляет площадь прямоугольника.

        Возвращает:
        Площадь круга, если радиус положительный.
        Генерирует ValueError, если радиус отрицательный.
        """
        if self.radius <= 0:
            raise ValueError(
                "Ошибка данных! Площадь не может быть отрицательной!")
        return pi * self.radius**2


crl = Circle(60)
print(crl.area())

# ****************************************************


class BankAccount:
    """Класс для имитации банковского кошелька"""

    def __init__(self, balance: int):
        """
        Инициализация кошелька с заданным балансом.

        Аргументы:
            balance (number): баланс кошелька (должен быть положительным).
        """
        self.balance = balance

    def deposit(self, amount: int):
        """
        Пополнение кошелька
        Аргументы:
            amount (number): средства пополнения кошелька (должен быть положительным)
        """
        self.balance += amount

    def withdraw(self, amount: int):
        """
        Расход кошелька

        Генерирует:
            ValueError: Если расход больше баланса.
        """
        if self.balance < amount:
            raise ValueError(
                "Ошибка данных! В вашем кошельке недостаточно средств!")
        self.balance -= amount

    def get_balance(self):
        """
        Возвращает баланс кошелька
        """
        return (self.balance)


card = BankAccount(600000)
print(card.get_balance())
card.deposit(45000)
print(card.get_balance())
card.withdraw(9000)
print(card.get_balance())
card.withdraw(9000000)

# ****************************************************


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


# ****************************************************


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f'Название книги: {self.title}, автор: {self.author}'

# my_book = Book('Преступление и наказание', 'Ф.М. Достоевский')
# print(my_book.display_info())


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def display_info(self):
        return f'Название книги: {self.title}, автор: {self.author}, размер файла: {self.file_size}'


my_book = Book('Му-му', 'И.С. Тургенев')
print(my_book.display_info())
print()
my_ebook = EBook('Преступление и наказание', 'Ф.М. Достоевский', '100kB')
print(my_ebook.display_info())


# ****************************************************

class Shape:
    def __init__(self):
        pass

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, height, base):
        super().__init__()
        self.height = height
        self.base = base

    def area(self):
        return (self.height * self.base) / 2


def area_of_figure(figure: str, data: str):
    if figure == 'круг' and data.isdigit():
        circle = Circle(int(data))
        print(f'Площадь круга: {circle.area()}')

    elif figure == 'прямоугольник' and data:
        w, h = map(int, data.split())
        rect = Rectangle(w, h)
        print(f'Площадь прямоугольника: {rect.area()}')

    elif figure == 'треугольник' and data:
        h, b = map(int, data.split())
        triag = Triangle(h, b)
        print(f'Площадь треугольник: {triag.area()}')
    else:
        print('Некорректный ввод')


fg = input('Введите название фигуры(круг, прямоугольник или треугольник): ')
data = input(
    'Введите данные выбранной фигуры (радиус / ширина высота / высота основание): ')
area_of_figure(fg, data)

# ****************************************************


class matrix:
    def __init__(self, n=0, m=0):
        self.n = n
        self.m = m
        self.matrix = []
        for i in range(self.n):
            self.matrix.append([])
            for j in range(self.m):
                self.matrix[i].append(0)

    def minput(self):
        self.n = int(input())
        self.m = int(input())
        for i in range(self.n):
            self.matrix.append([int(elem) for elem in input().split()])

    def mprint(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(str(self.matrix[i][j]).ljust(3), end='')
            print()

    def transpose(self):
        new = matrix()
        new.matrix = []
        for i in range(self.m):
            new.matrix.append([])
            for j in range(self.n):
                new.matrix[i].append(self.matrix[j][i])
        return new

    def trace(self):
        summa = 0
        for i in range(self.n):
            summa += self.matrix[i][i]
        return summa

    def greater_than_average(self):
        l = [0 for _ in range(len(self.matrix))]
        average = 0
        for i in range(self.n):
            for j in range(self.m):
                average += self.matrix[i][j]
            average //= self.m
            for j in range(self.m):
                if (self.matrix[i][j] > average):
                    l[i] += 1
            average = 0
        return l

    def maximum_in_area_1(self):
        maximum = self.matrix[0][0]
        for i in range(self.n):
            for j in range(i + 1):
                if (maximum < self.matrix[i][j]):
                    maximum = self.matrix[i][j]
        return maximum

    def maximum_in_area_2(self):
        maximum = self.matrix[0][0]
        for i in range(self.n):
            for j in range(self.m):
                if (maximum < self.matrix[i][j] and ((i >= j and i <= self.n - 1 - j) or (i <= j and i >= self.n - 1 - j))):
                    maximum = self.matrix[i][j]
        return maximum

    def u_quarter(self):
        l = []
        for i in range(self.n):
            for j in range(self.m):
                if ((i < j and i < self.n - 1 - j)):
                    l.append(self.matrix[i][j])
        return l

    def r_quarter(self):
        l = []
        for i in range(self.n):
            for j in range(self.m):
                if ((i < j and i > self.n - 1 - j)):
                    l.append(self.matrix[i][j])
        return l

    def d_quarter(self):
        l = []
        for i in range(self.n):
            for j in range(self.m):
                if ((i > j and i > self.n - 1 - j)):
                    l.append(self.matrix[i][j])
        return l

    def l_quarter(self):
        l = []
        for i in range(self.n):
            for j in range(self.m):
                if ((i > j and i < self.n - 1 - j)):
                    l.append(self.matrix[i][j])
        return l

    def multiplication_table(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = i * j

    def maximum_in_the_table(self):
        maximum = self.matrix[0][0]
        max_i, max_j = 0, 0
        for i in range(self.n):
            for j in range(self.m):
                if (maximum < self.matrix[i][j]):
                    maximum = self.matrix[i][j]
                    max_i, max_j = i, j
        return (max_i, max_j)


mult = matrix()
mult.minput()
print(*mult.maximum_in_the_table())

# ****************************************************


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
