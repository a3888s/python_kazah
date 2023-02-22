# Функції.

# Модулі в Python

# Імпорти файлів та модулів

# 1-вид імпорта

# from functions import get_sum

# print(get_sum(10,20))

# 2-вид імпорту

# import functions # імпортується весь файл та його вміст

# r = functions.get_sum(20,20)
# print(r)

# Застосування AS в імпортах

# Перший випадок коли назва фалу дуже велика

# from functions import get_numbers_division_result as get_div

# print(get_div(10,2))

# другий випалок використання AS в імпортах

# def get_list_sum(numbers):
#     result = 0
#     for i in numbers:
#         r += i
#     return r

# from functions import get_list_sum as get_numbers_sum

# Якщо в одином файлі використовується функції чи класи з схожими назвами
# Можливо через as перейменовуємо один, щоь не було помилоу в коді.

# Стандартна бібліотека Python
# В Python існує свій список готових бібліотек, які встановлюються
# під час загрузки Python.

# Кожна із бібліотек проходить перевірку від спільноти та розробників Python.
# 

# datetime

# from datetime import datetime

# print(datetime.now())

# time1 = datetime.strptime("2022-06-24", "%Y-%m-%d")
# time2 = datetime.strptime("2022-10-15", "%Y-%m-%d")
# print(time2-time1)

# now = datetime.now()
# print(now.strftime("%H:%M %d/%m/%Y"))

# Модуль math в Python

# from math import factorial, ceil, floor, pi

# print(factorial(5))
# print(ceil(10.1)) # Заокруглює число в більшу степінь
# print(floor(10.9))# Заокруглює число в менщу степінь
# print(pi) # отримуємо pi

# Модуль random
# from random import randint, random, shuffle, choice

# # randint( ) - рандомне ціле число в діапазоні
# r = randint(100,200)
# print(r)

# random() - рандомне не ціли число до 0
# r = random()
# print(r)

# shuffle - рандомно перемішує
# numbers = [1,2,3,4,5]
# shuffle(numbers)
# print(numbers)

# choice - вибирає рандомно елемент із списку
# names = ["Nurlan", "Aman", "Эрмак"]
# n = choice(names)
# print(n)

# Модуль os - Operation System - працює з операційною системою пк
# import time
# import os

# # print("JavaScript is the best")
# # time.sleep(10)
# # os.system("cls")
# # print("Python is the best")

# print(os.path.abspath(__file__))

# import turtle

# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

# import turtle
# loadWindow = turtle.Screen()
# turtle.speed(2)
 
# for i in range(100):
#     turtle.circle(5*i)
#     turtle.circle(-5*i)
#     turtle.left(i)
 
# turtle.exitonclick()

# Робота з Pip

# from prettytable import PrettyTable

# table = PrettyTable()

# table.field_names = ["name", "points"]
# data = [
#     ["Askar", 90],
#     ["Ali", 20],
#     ["Anna", 98],
#     ["Osmon", 50]
# ]

# table.add_rows(data)
# print(table)


# Тестування pandas та matplotlib

# import pandas as pd
# import matplotlib.pyplot as plt

# data = {
#     "days": [1,2,3,4,5,6],
#     "kg": [99,94,90,87,85,80]
# }
# dt = pd.DataFrame(data, columns=["days", "kg"])

# dt.plot(x="days", y="kg", kind="line")
# plt.show()

# Анонімні функції - lambda

# звичайна функція python
# def get_sum(a,b):
#     return a+b

# # аноніміні фунції
# summa = lambda x,y: x+y
# # lambda функція завжи пишиться в одну строку.

# print(summa(10,5))

# lymbda функція з умовою
# get_max = lambda x,y: x if x > y else y
# print(get_max(100,50))

# фнкція filter()
# def is_even(x):
#     if x % 2 == 0:
#         return True
#     return False

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_numbers = list(filter(is_even, numbers))
# print(even_numbers)

# even_numbers = list(filter(lambda x: True if x % 2 == 0 else False, numbers))
# print(even_numbers)

# Напишіть функцію з фільтром для фільтрації великих та малих букв
# letters = ["A", "b", "C", "c", "E", "h", "Z", "L", "I"]

# uppers_list2 = list(filter(lambda l: True if l.isupper() else False, letters))
# print(uppers_list2)

# def is_letters(x):
#     if x == x.upper():
#         return True
#     return False

# even_letters = list(filter(is_letters, letters))
# print(even_letters)

# Функція map() - застосовує до списку елементів вказану функцію та повертає список

# numbers = ["1","2","3","4","5"]

# int_numbers = list(map(int, numbers))
# print(int_numbers)

# letters = ["a","b","c","d","e","f","g"]
# # Завдання застосуйте функцію map иа створіть список букв великими.

# u_letters = list(map(str.upper, letters))
# print(u_letters)

# numbers = list(range(1,20))
# # def get_square(x):
# #     return x ** 2

# # square_list = list(map(get_square, numbers))
# # print(square_list)

# square_list = list(map(lambda x: x**2, numbers))
# print(square_list)

# i = 5
# x = i if i % 2 == 0 else 0
# print(x)