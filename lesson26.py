# people = [
#     ('Johnny', 22),
#     ('Adam', 18),
#     ('Mark', 12),
#     ('Jack', 14),
#     ('Sam', 20)
# ]

# # def is_adult(p):
# #     return p[1] >=18
# # adult_list = list(filter(is_adult, people))
# # print(adult_list)

# adult_list = list(filter(lambda p: p[1]>=18, people))
# print(adult_list)

# Зберігання в змінну через умову.

# text = input("Введіть текст: ")

# message = text if text else "Пусто"
# print(message)


# Створення списку через for та if

# List comprehensions - генерація списку
# numbers = [i for i in range(1,20)]
# print(numbers)
# aquare_list = [i**2 for i in range(1,20)]
# print(aquare_list)

# Створення list comprehensions через умову if
# even_numbers = [x for x in range(1, 20) if x % 2 == 0]
# print(even_numbers)

# products = ["Milk", "Breaf", "Orange", "Coffee"]
# uper_list = [p.upper() for p in products]
# print(uper_list)

# Завдання

# names = ["Рамазан", "Нікіта", "Аміна", "Аделя", "Тілек"]
# len_names = [f"{n}-{len(n)}" for n in names]
# print(len_names)

# names = ["Рамазан-20", "Нікіта-17", "Амін-16", "Аделя-22", "Тілек-25"]
# # Завдання.
# # Використовуючи list comprehensions і умову, виведіть тільки тих
# # кому більше 18

# max_names = [n for n in names if int(n.split("-")[1]) >= 18]
# print(max_names)

# all() - Перевіряє що в списку всі єлементи повертаються True

# x_list = [True, True, True, True]
# print(all(x_list))

# my_list = ["Аскар", "Антон", "Фатіма"]
# print(all(my_list))

# any() - Повертає True, якщо хочаб один із елементів поверне True

# x_list = [False, False, False, True]
# print(any(x_list))

# my_list = ["", None, False, "", [], {}, 1]
# print(any(my_list))

# Функція zip() - дай можливість перебору двох списків

# names = ["Askar", "Aman", "Faiza"]
# numbers = [1,2,3]

# print(list(zip(names, numbers)))

# for x,y in zip(names, numbers):
#     print(x,y)    

# Функція enumerate

# products = ["Milk", "coffee", "orange", "bread", "beer"]

# for i, product in enumerate(products, start=1):
#     print(f"{i}) {product}")

# бібліотека itertools

# import itertools
# numbers = [1,2,3,4,5]

# print(list(itertools.combinations(numbers, 3)))

# print(len(list(itertools.combinations_with_replacement(numbers, 100))))