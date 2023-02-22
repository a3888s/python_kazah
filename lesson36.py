# Декоратори методів класів.

# property - це декоратор методу, який перетворює метод в інформативний атрибут

# class Person:
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age =age
#
#     @property
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     @property
#     def is_adult(self):
#         if self.age >= 18:
#             return True
#         return False
#
#     def get_info(self):
#         return "Person class"
#
#
# p1 = Person("John", "Smith", 20)
# print(p1.first_name)
# print(p1.get_info())
# print(p1.full_name)
# print(p1.is_adult)

# classmethod(): - декоратор методів класу.
# Смисл декоратора, щоб зробити можливим виклик методу із класу.


# class Calculator:
#
#     @classmethod
#     def add(cls, n1, n2):
#         return n1+n2
#
#     @classmethod
#     def sub(cls, n1, n2):
#         return n1-n2
#
#     def get_info(self):
#         return "I am calculator class"
#
#
# result = Calculator.add(10, 20)
# print(result)
# result2 = Calculator.get_info()
# print(result2)

# Staticmethod - декоратор методів класу, який робить метод незалежним від класу та об'єкту.
# метод незалежний від класу чи об'єкту.


# class Person:
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @staticmethod
#     def is_adult(age):
#         if age >= 18:
#             return True
#         return False
#
#
# p1 = Person("John", "Smith")
# print(p1.first_name)
# print(p1.is_adult(50))
# print(Person.is_adult(15))


# різниця між атрибутами класу та атрибутами об'єкта.

# class SomeClass:
#
#     name = "My name is SomeClass"
#
#     def __init__(self, someattribute):
#         # Атрибути об'єкту
#         # в методі __init__ оголошуються тільки атрибути об'єкту.
#         self.someattribute = someattribute
#         self.attr2 = 0
#
#
# someobject = SomeClass("Somename")
# print(someobject.attr2)
# # print(SomeClass.attr2) - не доступні
# print(SomeClass.name)
# print(someobject.name)
# # __init__ - це конструктор об'єкта, Тому що саме він викликається під час створення об'єкта і додає атрибути для
# # об'єкту.
# object2 = SomeClass("Object2")
# print(object2.name)
#
# object2.name = "Someclass Attribute was changed."
# print(someobject.name)
# print(object2.name)
#
# SomeClass.name = "Someclass Attribute was changed."
# print(someobject.name)
# print(object2.name)

















