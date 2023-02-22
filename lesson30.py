# # Атрибути за замовчуванням
#
# class Hero:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # Атрибути об'єкту за замовчуванням
#         self.health = 100
#         self.protection = 50
#         self.damage = 4
#         self.weapon = None
#         self.level = 1
#
#     def get_info(self):
#         print(f"Ім'я персонажу: {self.name}")
#         print(f"Життя: {self.health}")
#         print(f"Броня: {self.protection}")
#
#     def update_level(self):
#         print("Збільшення рівня гравця...")
#         self.level += 1
#         self.health += 5
#         self.damage += 2
#         self.get_info()
#
#     def attack(self, enemy):
#         print(f"{self.name} атакує...{enemy.name}")
#         enemy.health -= self.damage
#         print(f"{enemy.name} отримав {self.damage} урон...")
#         enemy.get_info()
#
#
# batman = Hero("Bruce Wayne", 40)
# superman = Hero("Clark Rent", 30)
# superman.update_level()
#
# for i in range(1, 11):
#     superman.attack(batman)

# Перевантаження методів

# Магічний(Дандер) методи.
# Це метод, який має двойне підкреслення з двух сторін
# Вони налаштовують поведінку об'єкту в python коді


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     # Дандер метод який повертає імя об'єкту
#     def __str__(self):
#         return self.name
#
#
# khamza = Person("Khamza")
# nestan = Person("Nestan")
# print(khamza)
# print(nestan)
#
# class Number:
#
#     def __init__(self, n):
#         self.n = n
#
#     def __add__(self, other):
#         return self.n + 10
#
#     def __truediv__(self, other):
#         return
#
#
# n1 = Number(10)
# print(n1+15)
# print(n1/10)

# class PositiveNumberList:
#     def __init__(self):
#         self.numbers = []
#
#     def add_number(self, n):
#         if type(n) == list:
#             for i in n:
#                 if i % 2 == 0:
#                     self.numbers.append(i)
#         else:
#             if n % 2 == 0:
#                 self.numbers.append(n)
#             else:
#                 pass
#
#     def __iter__(self):
#         for i in self.numbers:
#             yield i
#
#     def __str__(self):
#         return f"{self.numbers}"
#
#
# my_list = PositiveNumberList()
# my_list.add_number(6)
# my_list.add_number(10)
# my_list.add_number(7)
# my_list.add_number([12, 15, 20])
# print(my_list)
# summa = 0
# for i in my_list:
#     summa += i
# print(summa)

# def get_names():
#     names = ["Nazar", "Nuraiym", "Aikan", "Amina"]
#     for i in names:
#         yield i
#
#
# for i in get_names():
#     print(i)

# Завдання. Створіть класс гаманець.
# Перевизначить дандер метод __add__, __sub__
# створіть атрибут balance.
# При сумуванні через оператор + в balance повинна додатись сумма.
# Якщо сумма, котрі додаються від'ємні, то виведіть помилку.
# При використанні оператора мінус. Відніміть від balance. Сумму.

# class Wallet:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def __add__(self, other):
#         if other < 0:
#             print(f"Введіть позитивне число")
#         else:
#             self.balance += other
#             return self.balance
#
#     def __sub__(self, other):
#         self.balance -= other
#         return self.balance
#
#     def __str__(self):
#         return f"Сума на балансі: {self.balance}"
#
#
# my_wallet = Wallet(0)
#
# my_wallet + 12
# print(my_wallet)
#
# my_wallet + 12
# print(my_wallet)
#
# my_wallet - 10
# print(my_wallet)
#
# my_wallet + (-12)
# print(my_wallet)
#
# my_wallet - 10
# print(my_wallet)
