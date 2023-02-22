# ООП-об'єктно орієнтоване програмування

# Основи ООП:
# 1) Класс
# 2) Обєкт
# 3) Методи
# 4) Атрибути
# dog_date = {
#     "name": "Rex",
#     "age": 5
# }
#
#
# def sit():
#     print(f"{dog_date['name']} сів...")
#
#
# sit()

# класс для створення об'єкта Dog
# class Dog:
#     def __init__(self, name, age):
#         # Оголошення атрибутів
#         self.name = name
#         self.age = age
#
#     # Всі функції оголошення в середині класів називається методами
#     def sit(self):
#         print(f"{self.name} сидить...")
#
#
# # Створення об'єкта на основі класу
# dog = Dog("Willie", 6)
# dog.sit()
#
# dog2 = Dog("Rex", 3)
# dog2.sit()

# Описуємо дім за допомоги ООП

# class House:
#     def __init__(self, address, width, length, rooms_count, price, owner):
#         self.address = address
#         self.width = width
#         self.length = length
#         self.rooms_count = rooms_count
#         self.price = price
#         self.owner = owner
#
#     def get_house_area(self):
#         print(f"Площа будинку: {self.width*self.length} кв. метрів")
#
#     def get_info(self):
#         print("Адрес", self.address)
#         print("Кількість кімнат", self.rooms_count)
#         print("Ціна", self.price)
#         print("Власник", self.owner)
#
#     def change_owner(self, new_owner):
#         self.owner = new_owner
#         print(f"Новий власник: {new_owner}")
#
#
# house = House("Гуцала 3", 10, 20, 6, 100_000, "a3888s")
# house.get_house_area()
# house.get_info()
# house.change_owner(new_owner="Anna")
# house.get_info()

# class Person:
#     def __init__(self, name, age, cash, weight, salary):
#         self.name = name
#         self.age = age
#         self.cash = cash
#         self.weight = weight
#         self.salary = salary
#
#     def earn_money(self, value):
#         self.cash += value
#         print(f"{self.name} заробив {value} грн")
#
#     def get_cash_info(self):
#         print(f"Гроші на рахунку: {self.cash} грн")
#
#     def get_salary(self):
#         self.cash += self.salary
#         print(f'Вам поступила заробітня плата в розмірі {self.salary} грн')
#
#     def buy(self, product, price):
#         if price <= self.cash:
#             print(f"{self.name} купив {product} за {price} грн")
#             self.cash -= price
#         else:
#             print("У вас не вистачає коштів на рахунку!")
#
#
# askar = Person("Askar", 29, 40000, 80, 30_000)
# askar.get_cash_info()
# askar.buy("PlayStation 4", 25000)
# askar.get_cash_info()

# Класс — це блок оголошення через команду class
# Метод — це функція оголошення всередині классу
# Атрибут — це данні, які знаходяться в методі def __init__()
# Обєкт(Екзимпляр классу) — це створений на основі классу змінна
# self — це сполучна ланка в середині классу. Це посилання на об'єкт.

# Створіть класс Employee. Який має атрибути: name, salary, position(посада).
# Добавте методи
# new_position(position_name) - даний метод змінює позицію працівника
# raise_salary(amount) - даний метод збільшує зарплату працівника
# get_info() - виводить інформацію працівника
# Створіть в кінці обєкт і протестуйте його.

# class Employee:
#     def __init__(self, name, salary, position):
#         self.name = name
#         self.salary = salary
#         self.position = position
#
#     def get_info(self):
#         print(f"Ім'я: {self.name}")
#         print(f"Посада працівника: {self.position}")
#         print(f"Баланс: {self.salary}")
#
#     def new_position(self, position_name):
#         if position_name == self.position:
#             print(f"Неможливо змінити обрану посаду {position_name}")
#         else:
#             self.position = position_name
#             print(f"Нова позиція {position_name}")
#
#     def raise_salary(self, amount):
#         self.salary += amount
#         print(f"Нараховано {amount}")
#
#
# a3888S = Employee("a3888s", 0, "Директор")
# a3888S.get_info()
# a3888S.new_position("Директор")
# a3888S.get_info()
# a3888S.raise_salary(10000)
# a3888S.get_info()

# Необов'язкові атрибути классу
# class Car:
#
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#         self.odometr = 0
#         self.tank = 40
#
#     def drive(self):
#         if self.tank > 0:
#             print("машина рухається")
#             self.odometr += 100
#             self.tank -= 11
#         else:
#             print("Потрібно заправитись")
#
#     def tanking(self, value):
#         print("Ви заправились")
#         self.tank += value
#
#     def get_info(self):
#         print(f"Бензин: {self.tank}")
#         print(f"Пробіг: {self.odometr}")
#
#
# toyota = Car("Toyota Camry 75", "Black")
# toyota.drive()
# toyota.drive()
# toyota.drive()
# toyota.tanking(30)
# toyota.drive()
# toyota.get_info()
