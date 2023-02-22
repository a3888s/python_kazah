# ТЕМА: Функції.

# def function_name():
    # тіло функціх чи блок коду

# def - це оголошення функції від слова defenition
# після іде назва функції, дужки та двікрапки.

# Яке імя повинно бути у функції:
# 1) Імя повинно містити тільки маленікі букви
# 20 Імя функції повинно починатися з алфавітних символів чи "_"
# 3) Назва функції повинно бути в формі дієслова.
# Приклад: send_message(), get_user(), update_date(), save_data()
# 4) Якщо функція містить декілька слів, бажано розділити
# через знак "_"

# Створення функції
# def greet_user():
#     print("Hello !!!")


# function call - визов функції. Це коли функція активується через його імя в коді.

# greet_user() # () - дужки обовязкові!
# greet_user()
# greet_user()
# Кількість викликів функцій необмежено.

# Передача інформації (аргументів) всередину функцій.

# def greet_user(name):
#     # name - це обовязковий аргумент функції
#     # при визові обовязково потрібно йому передати дані,
#     # який він очікує
#     name = name.upper()
#     print(f"Hello, {name}")

# first_name = input("Напишіть ваше імя: ")
# greet_user(name=first_name)

# def greet_user2(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     print(f"Привіт {full_name}")

# # Іменована передача данних в аргумент
# greet_user2(first_name="Ali", last_name="Osmonov")

# # Позиційна передача даних в аргумент
# greet_user2("Ali", "Osmanov")

# Завдання - 1
# Запитайте у користувача його імя і вік через input().
# Створіть функцію get_info(), яка отримує імя та вік
# І склдає з ним речення в вигляді.
# My name is John. I am 19 years old.

# def get_info(name, old):
#     print(f"My name is {first_name}. I am {years} years old.")
# first_name = input("Введіть ваше ім'я: ")
# years = input("Скільки вам років: ")
# get_info(name=first_name, old=years)

# # Логіка всередині функції:
# def check_user_age(age):
#     if age <16:
#         print("Ваша знижка 50%")
#     elif age < 18:
#         print("Ваша знижка 20%")
#     else:
#         print("Ви оплачуєте повну суму")

# check_user_age(age=19)
# check_user_age(16)

# Створіть функцію для перевірки парності або непарності.
# Вмя функції check_even(number): функція повинна перевірити і роздрукувати на екран
# вид числа. Парна чи не парна.


# def check_even(number):
#     if n_input % 2 == 0:
#         print(f"Число {n_input} ціле!")
#     else:
#         print(f"Число {n_input} не ціле!")
# n_input = int(input("Введіть число для перевірки: "))
# check_even(n_input)


# Створіть функцію get_square(n):
# яка приймає число та зводить його в квадрат
# На екран роздрукуйте результат із функції.

# def get_square(n):
#     n_sum = n_input**2
#     print(f"Квадрат числа {n_input} дорівнює {n_sum}: ")
# n_input = int(input("Введіть Ваше число: "))
# get_square(n_input)

# Створіть функцію get_procent(n,p). Приймає два оргументи.
# n - число, р - це процент, який потрібно знайти із числа n.

# def get_procent(n,p):
#     result = n_input*p_input / 100
#     print(f"{p_input} відсотків від числа {n_input} дорівнює {result}: ")
# n_input = int(input("Введіть число: "))
# p_input = int(input("Введіть відсоток: "))
# get_procent(n_input, p_input)

# Завдання
# Створіть функцію,
# Яка отримує текст і повертає кількість маленьких та великих букв в тексті.
# get_letters_count(text)

# Створіть функцію, яка отримує
# 