# Принципи ООП
# 1) Наслідування
# 2) Інкапсуляція
# 3) Поліморфізм
# 4) Абстракція

# Тема: поліморфізм

# class Cat:
#
#     def make_noise(self):
#         print("Мяу Мяу")
#
#
# class Dog:
#
#     def make_noise(self):
#         print("Гав Гав")


# Поліморфізм це принцип ООП при якому однакові цілі досягаються різни шляхом

# print(10+10)
# print("Hello "+"World")

# class Person:
#
#     def be_rich(self):
# Створіть батьківський клас Shape. Який має метод area().
# Завдання створити два класи Circle, Triangle та перепишіть в них метод area() під кожну фігуру.
# Також запитуйте визначенні атрибути для кожного виду фігури

# class Shape:
#
#     def area(self):
#         pass
#
#
# class Circle(Shape):
#
#     def __init__(self, r):
#         self.r = r
#
#     def area(self):
#         return 3.14 * self.r**2
#
#
# class Triangle(Shape):
#
#     def __init__(self, a, h):
#         self.a = a
#         self.h = h
#
#     def area(self):
#         return self.a/2*self.a*self.h
#
#
# name = Circle(10)
# print(name.area())
# name1 = Triangle(10, 15)
# print(name1.area())

# Абстракція в Python

# from abc import ABC, abstractmethod


# Абстрактний клас
# class Animal(ABC):

    # @abstractmethod
    # def make_noise(self):  # Абстрактний метод
    #     pass
    #
    # Абстрактний це клас який містить абстрактні методи, які вказують
    # на методи котрі повинні бути в наслідуюмих класах
    # Абстрактні методи не містять реалізації коду, а тільки служать структурою для майбутніх класів.
    # Абстрактні класи не можуть мати об'єкти


# class Dog(Animal):
#
#     def make_noise(self):
#         print("Гавкає")
#
#
# class Cat(Animal):
#
#     def make_noise(self):
#         print("М'явкає")
#
#
# d = Dog()
# cat = Cat()
# d.make_noise()
# cat.make_noise()

# Створіть клас Car з публічними методами start_engine і stop_engine, які дозволяють користувачам
# запускати та зупиняти двигун автомобіля.

# Додайте приватне поле _engine_started, яке зберігає стан двигуна (запущений чи зупинений)

# Створіть приватний метод _ensure_engine_stopped, який буде перевіряти, чи зупинений двигун.
# Якщо двигун запущений, метод повинен повідомити про помилку.

# В методі start_engine встановіть стан двигуна True і викличіть метод _ensure_engine_stopped,
# щоб переконатись, що двигун зупинено.

# В методі stop_engine встановіть стан двигуна False.

# class Car:
#
#     _engine_started = False
#
#     def _ensure_engine_stopped(self):
#         if self._engine_started:
#             print("Двигун запущено")
#         else:
#             print("Двигун зупинено")
#
#     def start_engine(self):
#         self._engine_started = True
#
#     def stop_engine(self):
#         self._engine_started = False
#
#
# car = Car()
# car._ensure_engine_stopped()
# car.start_engine()
# car._ensure_engine_stopped()
# car.stop_engine()
# car._ensure_engine_stopped()





















