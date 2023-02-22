# Необовязкові аргументи функції

# def get_fullname(first, last, middle=""):
#     # аргумент middle_name - не обовязковий.
#     # під час оголошення аргументу ми прирівняли його до пустого значення.
#     # Тепер цей аргумент став необовязковим при вклику функції.
#     if middle:
#         full_name = f"{first} {last} {middle}"
#     else:
#         full_name = f"{first} {last}"
#     return full_name
# print(get_fullname("Abi", "Toloev"))
# print(get_fullname("John", "Smith", "Saimon"))

# Аргумент по замовчуванню в фенкції

# def get_porcent(number, porcent=20):
#     result = number*porcent / 100
#     return result
# print(get_porcent(200)) # Не передаємо procent, тому що він рівний 20 за замовченням
# print(get_porcent(200, 50))

# Робота з списками в функції.


# def change_list(name_list):
#     new_names = []
#     while name_list:
#         name = name_list.pop()
#         name = name.upper()
#         new_names.append(name)
#     return new_names

# names = ["Ali", "Askar", "Sveta", "Alina", "Anton"]
# print(change_list(names.copy()))

# print("Наш список, який вілправили в функцію: ", names)

# Довільне кількість аргументів в фнкції.

# 1) *args - довільна кількість позиційних елементів

# def get_toppings(size, *args):
#     print(size)
#     print(args)
#     print("Інгрідієнти: ")
#     for i in args:
#         print(i)
# get_toppings("Сир", "Папероні")

# *args - може приймати тільки позиційні аргументи

# **kwargs - необмежена кількість іменованих аргументів

# def get_user_info(**kwargs):
#     print(kwargs)
#     print("User info: ")
#     for key, value in kwargs.items():
#         print(f"{key}: {value }")

# get_user_info(name="Abi", age=20, address="Ahunbaeva 98", city="Bishkek")

# def get_numbers():
#     return 1,2,3
# # якщо функція повертає декілька значень одночасно через return
# # Ці декілька аргументів будуть вставленні в кортеж (tupple) і повернуті із функції
# print(get_numbers())

# def get_info():
#     return "Ala", "Osmonov", 10, [1,2,3,4,5]
# print(get_info())

