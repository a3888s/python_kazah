# Тема: Робота з умовами (if)

# Використовуємо методи для умов.
# letters = ["a", "A", "b", "B", "c", "C"]
# upper_letters = []
# lower_letters = []
# for l in letters:
#     if l.isupper():
#         upper_letters.append(l)
#     else:
#         lower_letters.append(l)

# print(upper_letters)
# print(lower_letters)

# Команда if(умова) може працювати не тільки з оператрами поріdняння, але
# і з методами типів даних, які повертають True або False
#  Конструкція if-elif-else.
# Якщо в завданні потрібн поставити декілька умов.
# Використовуємо додаткові конструкції elif
# Умова в атракціоні

# age = int(input("ВВедіть вік: "))

# if age<=4:
#     print("Бесплатно")
# elif age <= 18:
#     print("50% від ціни")
# else:
#     print("Повна сума")

# ПРАВИЛО. В КОНСТРУКЦІЇ if-elif-else(недивлячись на кількість умов)
# за один раз може спрацювати лише одина умова.
# Виконання декількох умов в одній конструкції виключено.


# Завдання. Сортквання символів в списку в окремі списки.

# symbols = ["a", "A", "b", "B", "1", "2", "D", "d", "3", "4"]
# u_letters = []
# l_letters = []
# numers = []

# for s in symbols:
#     if s.isdigit():
#         numers.append(s)
#     elif s.isupper():
#         u_letters.append(s)
#     else:
#         l_letters.append(s)
# print(u_letters)
# print(l_letters)
# print(numers)

# Сортування по типу даних через умову.

# random_list = ["hell", "a", 120, 2.5, "word", 15, 10, "john", 0.156, 7.5]

# string_list = []
# numver_list = []
# float_list = []


# for r in random_list:
#     if type(r) == str:
#         string_list.append(r)
#     elif type(r) == int:
#         numver_list.append(r)
#     elif type(r) == float:
#         float_list.append(r)

# print(string_list)
# print(numver_list)
# print(float_list)

# Перевірка на парність та не парність чисел.

# number = int(input("Введыть число: "))

# if number % 2 == 0:
#     print("Ціле")
# else:
#     print("Не ціле")

# Завдання 1:
# Існує список чисел, котрі потрібно відсортувати на цілі та не цілі числа.
# numbers = [10, 3, 7, 5, 6, 8, 15, 17, 20, 14]
# even_numbers = [] # для цілих
# odd_numbers = [] # для не цілих

# for n in numbers:
#     if n % 2 == 0:
#         even_numbers.append(n)
#     else:
#         odd_numbers.append(n)
# print(even_numbers)
# print(odd_numbers)

# Завдання - 2
# Існує список чисел. Потрібно відсортувати на 
# позитивні та відємні числа.
# numbers = [-1, -5, 10, 15, -17, ]

# plus_numbers = []
# minus_numbers = []

# for n in numbers:
#     if n < 0:
#         minus_numbers.append(n)
#     else:
#         plus_numbers.append(n)
# print(plus_numbers)
# print(minus_numbers)

# Завдання - 3
# text = "ABCDabcd112299"
# # Знайдіть кількість великих літер, маленькиї літер, та кількість літер в цій строці
# # Виведіть на екран.
# # Приклад:
#     # Кількість великих букв: 10
#     # Кількість маленікиз букв: 5
#     # Кількість цифр: 3

# t_upper = []
# t_lower = []
# t_digital = []

# for t in text:
#     if t.isupper():
#         t_upper.append(t)
#     elif t.islower():
#         t_lower.append(t)
#     else:
#         t_digital.append(t)
# print(f"Кількість великих букв: {len(t_upper)}")
# print(f"Кількість маленьких букв: {len(t_lower)}")
# print(f"Кількість цифр: {len(t_digital)}")