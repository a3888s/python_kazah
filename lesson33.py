# ООП.Принципи ООП
# 1) Наслідування
# 2) Інкапсуляція
# 3) Поліморфізм
# 4) Абстракції

# Тема: Інкапсуляція
# види інкапсуляції:
# 1) Публічний (public)
# 2) Приватний (__private)
# 3) Захищений (_protected)
# class Person:
#     def __init__(self, name, age, salary):
#         self.name = name  # публічний атрибут без знаків підкреслення в імені
#         self.__cash = 0  # приватний атрибут має два знаки підкреслення на початку імені
#         self._age = age  # захищений атрибут має один знак підкреслення на початку імені
#         self._salary = salary  # захищений атрибут має один знак на початку імені
#
#     # Приватний метод
#     def __add_cash(self, amount):
#         self.__cash += amount
#
#     def get_salary(self):
#         self.__add_cash(self._salary)
#         print("Ви отримали заробітню плату")
#         print("Ваш баланс: ", self.__cash)
#
#     # Захищений метод в Python
#     def _get_age_info(self):
#         print(f"{self.name} is {self._age} years old.")
#
#
# person = Person("Askar", 22, 25_000)
# # print(person.name) - публічний атрибут повністю доступний для виклику
# # print(person._age) - захищений атрибут можемо викликати але не бажано
# # print(person.__cash) - приватний атрибут неможливо викликати
# # print(person.__add_cash(20000))
# person.get_salary()  # Додає кошти до нашого рахунку, який приватний і не може бути викликаний
# person._get_age_info()  # Захищений метод

# Створіть клас GemaMario(). Створіть у ньому атрибути name, __points.
# Створіть захищений метод __add_points(self, amount), які додають бали в атрибут __points.
# Додайте два публічних метода це catch_coin(), який додає 50 балів.
# kill_enemy() додає 100 балів
# атрибут для балів не повинен бути доступний із зовні та змінюватись тільки через catch_coin(), kill_enemy()
# Додайте також публічний метод, який повертає наявний стан балів у гравця.

# class GameMario:
#
#     def __init__(self, name):
#         self.name = name
#         self.__points = 0
#
#     def __add_points(self, amount):
#         self.__points += amount
#
#     def catch_coin(self):
#         self.__add_points(50)
#
#     def kill_enemy(self):
#         self.__add_points(100)
#
#     def get_info(self):
#         print(f"Бали: {self.__points}")
#
#
# user = GameMario("a3888s")
# user.catch_coin()
# user.get_info()
# user.kill_enemy()
# user.get_info()

# Вам необхідно реалізувати клас "Банківський рахунок", який буде містити наступні поля і методи:
# приватне поле __balance (баланс рахунку)
# приватне поле __owner (імя власника рахунку)
# публічний метод get_balance(), який повертає баланс рахунку
# публічний метод get_owner(), який повертає імя власнику рахунку
# публічний метод deposit(amount), який додає вказану суму до балансу рахунку
# публічний метод withdraw(amount), який знімає суму з балансу рахунку

# class BankAccount:
#
#     def __init__(self, __owner):
#         self.__owner = __owner
#         self.__balance = 0
#
#     def get_balance(self):
#         print(f"Баланс рахунку: {self.__balance} грн")
#
#     def get_owner(self):
#         print(f"Імя власника рахунку: {self.__owner}")
#
#     def deposit(self, amount):
#         self.__balance += amount
#
#     def withdraw(self, amount):
#         self.__balance -= amount
#
#
# user = BankAccount("a3888s")
# user.deposit(100_000)
# user.get_balance()
# user.withdraw(50_000)
# user.get_balance()

