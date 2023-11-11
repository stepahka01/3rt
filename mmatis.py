# class Book:
#
#     def __init__(self, name, author, isbn):
#         self.__name = name
#         self.__author = author
#         self.__isbn = isbn
#
#     def get_author(self):
#         return self.__author
#
#     def set_author(self, author):
#         self.__author = author
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_isbn(self):
#         return self.__isbn
#
#     def set_isbn(self, isbn):
#         self.__author = isbn
#
#
# b = Book('name', 'author1', '1234543736472')
# print(b.get_author())
# b.set_author('fnndbk')
# print(b.get_author())

#
# class Figure:
#     def __init__(self, coords, width, color):
#         self.coords = coords
#         self.width = width
#         self.color = color
#
#     def draw(self):
#         print(f'рисуем фигуру цветом {self.color} и шириной {self.width}')
#
#
# class Line(Figure):
#     def draw(self):
#         print(f'рисуем линию цветом {self.color} и шириной {self.width}')
#
#
# class Rect(Figure):
#     def __init__(self, coords, width, color, right):
#         super().__init__(coords, width, color)
#         self.right = right
#
#     def draw(self):
#         print(f'рисуем прямоугольник цветом {self.color} и шириной {self.width}. Прямоугольник {self.right}')
#
#
# class Ellips(Figure):
#     def draw(self):
#         print(f'рисуем эллипс цветом {self.color} и шириной {self.width}')
#
#
# f = Figure([1, 2, 3, 4, 5, 6], 2, 'black')
# f.draw()
# l = Line([1, 2, 3], 4, 'white')
# class Publication:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def display(self):
#         print('Название:', self.title)
#         print('Автор:', self.author)
#         print('Год выпуска:', self.year)
#
#
# class Book(Publication):
#     def __init__(self, title, author, year, isbn):
#         super().__init__(title, author, year)
#         self.isbn = isbn
#
#     def display(self):
#         super().display()
#         print(f'ISBN: {self.isbn}')
#
#
# class Magazine(Publication):
#     def __init__(self, title, author, year, issue_number):
#         super().__init__(title, author, year)
#         self.issue_number = issue_number
#
#     def display(self):
#         super().display()
#         print(f'Номер журнала: {self.issue_number}')
#
#
# def info(obj):
#     obj.display()
#
#
# p = Publication('Название1','Автор1',2015)
# b = Book('Название2','Автор2',2021,2003939300)
# m = Magazine('Автор3','Название3',2023,5)

import random
class MusicAlbum:

    def __init__(self,title,artist,release_year,genre,tracklist):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist

    def get_info(self):
        print(f'''
Название:{self.title}
Исполгнитель:{self.artist}
Год выпуска:{self.release_year}
Жанр:{self.genre}
Список треков:{self.tracklist}
''')

    def play_random_track(self):
        return random.choice(self.tracklist)

album4 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte",
                    ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex",
                     "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo",
                     "Hallomann"])
print("Название:", album4.title)
print("Исполнитель:", album4.artist)
print("Год:", album4.release_year)
print("Жанр:", album4.genre)
print("Треки:", album4.tracklist)
album4.play_random_track()


album4.get_info()
print(album4.play_random_track())









#1
import random
class MusicAlbum:

    def __init__(self, title, artist, release_year, genre, tracklist):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist

    def get_info(self):
        print(f'''
Название:{self.title}
Исполгнитель:{self.artist}
Год выпуска:{self.release_year}
Жанр:{self.genre}
Список треков:{self.tracklist}
''')

    def play_random_track(self):
        return random.choice(self.tracklist)


album4 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte",
                    ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex",
                     "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo",
                     "Hallomann"])


album4.get_info()
print(f'Воспроизводится трек:{album4.play_random_track()}')



2
class Student:
    def __init__(self,name, age, grade, scores):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores

    def average_score(self):
        return sum(self.scores)/len(self.scores)


student2 = Student("Егор Данилов", 12, "5B", [5, 4, 4, 5])
print("Имя:", student2.name)
print("Возраст:", student2.age)
print("Класс:", student2.grade)
print("Оценки:", *student2.scores)
print("Средний балл:", student2.average_score())



#3


class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def print_ingredients(self):
        print("Ингредиенты для", self.name + ":")
        for ingredient in self.ingredients:
            print("-", ingredient)

    def cook(self):
        print("Готовим", self.name)
        print(self.name, "готов")

spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
spaghetti.print_ingredients()
spaghetti.cook()

cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])
cake.print_ingredients()
cake.cook()




#4
class Publisher:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_info(self):
        print("Издательство:", self.name)
        print("Расположение:", self.location)

    def publish(self, message):
        print('Готовим "', message, '" к публикации в', self.name, '(', self.location, ')')


class BookPublisher(Publisher):
    def __init__(self, name, location, num_authors):
        super().__init__(name, location)
        self.num_authors = num_authors

    def publish(self, message, author):
        print('Передаем рукопись "', message, '", написанную автором', author, 'в издательство', self.name, '(', self.location, ')')


class NewspaperPublisher(Publisher):
    def __init__(self, name, location, num_pages):
        super().__init__(name, location)
        self.num_pages = num_pages

    def publish(self, message):
        print('Печатаем свежий номер со статьей "', message, '" на главной странице в издательстве', self.name, '(', self.location, ')')


publisher = Publisher("АБВГД Пресс", "Москва")
publisher.publish("Справочник писателя")

book_publisher = BookPublisher("Важные Книги", "Самара", 52)
book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")

newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
newspaper_publisher.publish("Новая версия Midjourney будет платной")


#5
class BankAccount:
    def __init__(self, balance, interest_rate):
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f'Внесение наличных на счет: {amount}')

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f'Снятие наличных: {amount}')
        else:
            print('Недостаточно средств на счете.')

    def add_interest(self):
        interest = self.__balance * self.__interest_rate
        self.__balance += interest
        self.__transactions.append(f'Начислены проценты по вкладу: {interest}')

    def history(self):
        for transaction in self.__transactions:
            print(transaction)

# создаем объект счета с балансом 100000 и процентом по вкладу 0.05
account = BankAccount(100000, 0.05)
# вносим 15 тысяч на счет
account.deposit(15000)
# снимаем 7500 рублей
account.withdraw(7500)
# начисляем проценты по вкладу
account.add_interest()
# печатаем историю операций
account.history()



#6
class BankAccount:
    def __init__(self, balance, interest_rate):
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f'Внесение наличных на счет: {amount}')

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f'Снятие наличных: {amount}')
        else:
            print('Недостаточно средств на счете.')

    def add_interest(self):
        interest = self.__balance * self.__interest_rate
        self.__balance += interest
        self.__transactions.append(f'Начислены проценты по вкладу: {interest}')

    def history(self):
        for transaction in self.__transactions:
            print(transaction)

# создаем объект счета с балансом 100000 и процентом по вкладу 0.05
account = BankAccount(100000, 0.05)
# вносим 15 тысяч на счет
account.deposit(15000)
# снимаем 7500 рублей
account.withdraw(7500)
# начисляем проценты по вкладу
account.add_interest()
# печатаем историю операций
account.history()


# 7
class Animal:
    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def voice(self):
        print(f'{self.name} подает голос')

    def move(self):
        print(f'{self.name} дергает хвостом')


class Dog(Animal):
    def __init__(self, name, species, legs, breed = 'собака'):
        super().__init__(name, species, legs)
        self.breed = breed

    def bark(self):
        print(f'{self.species} {self.name} лает')


class Bird(Animal):
    def __init__(self, name, species, legs, wingspan = '20см'):
        super().__init__(name, species, legs)
        self.wingspan = wingspan

    def fly(self):
        print(f'{self.species} {self.name} летает')


dog = Dog("Геральт", "доберман", 4)
bird = Bird("Вася", "попугай", 2)
dog.voice()
bird.voice()
dog.move()
bird.move()
dog.bark()
bird.fly()


#8
class Shape:
    def __init__(self, color):
        self.name = "геометрическая фигура"
        self.color = color

    def describe(self):
        print(f"Это {self.name}, цвет - {self.color}.")

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.name = "окружность"
        self.radius = radius

    def describe(self):
        print(f"Это {self.color} {self.name}. Радиус - {self.radius} см, цвет - {self.color}.")

    def area(self):
        return 3.14 * self.radius**2

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.name = "прямоугольник"
        self.length = length
        self.width = width

    def describe(self):
        print(f"Это {self.color} {self.name}. Длина - {self.length} см, ширина - {self.width} см, цвет - {self.color}.")

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.name = "треугольник"
        self.base = base
        self.height = height

    def describe(self):
        print(f"Это {self.color} {self.name} с основанием {self.base} см и высотой {self.height} см, цвет - {self.color}.")

    def area(self):
        return 0.5 * self.base * self.height

circle = Circle("красный", 5)
rectangle = Rectangle("синий", 3, 4)
triangle = Triangle("фиолетовый", 6, 8)

circle.describe()
rectangle.describe()
triangle.describe()

print(f"Площадь треугольника {triangle.area()}, окружности {circle.area()}, прямоугольника {rectangle.area()} см.")


#9
class Candy:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

class Chocolate(Candy):
    def __init__(self, name, price, weight, cocoa_percentage, chocolate_type):
        super().__init__(name, price, weight)
        self.cocoa_percentage = cocoa_percentage
        self.chocolate_type = chocolate_type

class Gummy(Candy):
    def __init__(self, name, price, weight, flavor, shape):
        super().__init__(name, price, weight)
        self.flavor = flavor
        self.shape = shape

class HardCandy(Candy):
    def __init__(self, name, price, weight, flavor, filled):
        super().__init__(name, price, weight)
        self.flavor = flavor
        self.filled = filled

chocolate = Chocolate(name="Швейцарские луга", price=325.50, weight=220, cocoa_percentage=40, chocolate_type="молочный")
gummy = Gummy(name="Жуй-жуй", price=76.50, weight=50, flavor="вишня", shape="медведь")
hard_candy = HardCandy(name="Crazy Фрукт", price=35.50, weight=25, flavor="манго", filled=True)

print("Шоколадные конфеты:")
print(f"Название конфет: {chocolate.name}")
print(f"Стоимость: {chocolate.price} руб")
print(f"Вес брутто: {chocolate.weight} г")
print(f"Процент содержания какао: {chocolate.cocoa_percentage}")
print(f"Тип шоколада: {chocolate.chocolate_type}")
print("\nМармелад жевательный:")
print(f"Название конфет: {gummy.name}")
print(f"Стоимость: {gummy.price} руб")
print(f"Вес брутто: {gummy.weight} г")
print(f"Вкус: {gummy.flavor}")
print(f"Форма: {gummy.shape}")
print("\nФруктовые леденцы:")
print(f"Название конфет: {hard_candy.name}")
print(f"Стоимость: {hard_candy.price} руб")
print(f"Вес брутто: {hard_candy.weight} г")
print(f"Вкус: {hard_candy.flavor}")
print(f"Начинка: {hard_candy.filled}")


#10
class Soldier:
    def __init__(self, name, rank, service_number):
        self.name = name
        self.__rank = rank
        self.__service_number = service_number

    def get_rank(self):
        return self.__rank

    def confirm_service_number(self, service_number):
        return service_number == self.__service_number

    def promote(self):
        if self.__rank == "рядовой":
            self.__rank = "ефрейтор"
            return f"{self.name} повышен в звании, он теперь {self.__rank}"
        return f"{self.name} не может быть повышен в звании"

    def demote(self):
        if self.__rank == "ефрейтор":
            self.__rank = "рядовой"
            return f"{self.name} понижен в звании, он теперь {self.__rank}"
        return f"{self.name} не может быть понижен в звании"

soldier1 = Soldier("Иван Сусанин", "рядовой", "12345")
print(f"Создан новый игровой персонаж типа Soldier с атрибутами: {vars(soldier1)}")
print(f"Персонаж {soldier1.name} имеет звание {soldier1.get_rank()}")
print(soldier1.promote())
print(soldier1.demote())


