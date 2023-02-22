# Дандер методи та перезавантаження методів

# Дандер це метод, який контролює поведінку класу і його об'єктів

# __init__ - це дандер метод.
# головне позначення дандер методу це двійні підкреслення з двух сторін

# class A:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):  # повертає імя об'єкту
#         return self.name
#
#     def __len__(self):  # змінює поведінку об'єкту при застосуванні до об'єкту функції len()
#         return len(self.name)
#
#     def __iter__(self):  # дає можливість додавати ітерацію до об'єкту
#         for i in self.name:
#             yield i
#
#     def __eq__(self, other):
#         # змінює поведінку класу на оператор ==
#         if isinstance(other, A):
#             return True
#         return False
#
#
# a = A("a3888s")
# print(a)
# print(len(a))
#
# # for i in a:
# #     print(i)
#
# a2 = A("HKJGFHGFJHGGKH")
# print(a == a2)


# class Number:
#
#     def __init__(self, n):
#         self.n = n
#
#     def __add__(self, other):
#         if isinstance(other, Number):
#             return self.n + other.n
#         elif type(other) == int:
#             return self.n + other
#         else:
#             raise TypeError("Invalid DFate!")
#
#
# n1 = Number(150)
# print((n1+250))
#
# n2 = Number(500)
# print(n1+n2)

# class Students:
#
#     def __init__(self, students_list):
#         self.students_list = students_list
#
#     def __contains__(self, item):
#         if item in self.students_list:
#             return True
#         return False
#
#
# students = Students(["Ермек", "Тилек", "Муслим"])
# print("Ермек" in students)


# class B:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self, *args, **kwargs):
#         return "Я обєкт класу, мене визвали"
#
#     def __add__(self, other):
#         if isinstance(other, B):
#             return self.name + other.name
#         raise TypeError
#
#
# b = B("A3888S")
# b2 = B("Bektur")
# print(b())
# print(b.__call__())
# print(b.__add__(b2))

# Напишіть класс EngAlphabet().
# Який має аргумент letters.
# Де зберігаються список всіх букв англійської мови

# __iter__(self)
# Використовуючи дандер методи додайте можливість перебирати об'єкт класу EngAlphabet отримуючи
# по одній букви алфавіту.

# Додайте із допомогою дандер методу перевірку, що буква являється англійською буквою
# являється англійською буквою.

# Напишіть дандер, який перевизначить поведінку на функцію len()
# та буде повертати довжину алфавіту.


# class EngAlphabet:
#
#     def __init__(self):
#         self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
#                         "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
#                         "W", "X", "Y", "Z"]
#
#     def __iter__(self):
#         for l in self.letters:
#             yield l
#
#     def __contains__(self, item):
#         if item in self.letters:
#             return True
#         else:
#             return False
#
#     def __len__(self):
#         return len(self.letters)
#
#
# eng = EngAlphabet()
# print(eng.__iter__())
# print(eng.__contains__("Д"))
# print(eng.__len__())


# Створіть клас EWallet.
# Даний клас має атрибути balance, де зберігається баланс рахунку
# Перевизначіть дандер метод, який працює з оператором +, -
# При застосуванні до об'єкту класу + і число, дане число повинно сумуватись до рахунку
# У випадку мінуса відніматись
# Додайте метод get_balance, який повертає баланс.
# wallet = EWallet(10_000)
# wallet+5_000
# wallet-10_000

# class EWallet:
#
#     def __init__(self, balance):
#         self.balance = balance
#
#     def __add__(self, other):
#         self.balance += other
#
#     def __sub__(self, other):
#         self.balance -= other
#
#     def get_balance(self):
#         print(self.balance)
#
#
# wallet = EWallet(10_000)
# wallet+5_000
# wallet.get_balance()
# wallet-10_000
# wallet.get_balance()

# Створіть класс Person().
# Person має атрибути name, age, height,
# Об'єкт класу person при застосуванні print до об'єкту повинен повертати name - def __str__(self)
# Перевизначіть дандер методи порівняння, щоб порівнюючи двух об'єктів person.
# порівняння проходило через іх вік
# При застосуванні до об'єкту person len(), він повинен повертати ріст цього person

class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return self.name

    def __gt__(self, other):
        if self.age > other:
            return self.name
        else:
            return self.name


p1 = Person("Askar", 30, 180)
p2 = Person("Osmon", 40, 175)

print(p1)
print(p1>p2)


