# ТЕМА: Змінні, Тип данних - Строка.

# Змінні

# name = "a3888s" # створення змінної name
# # = - Оператор присвоєння
# print(name)
# Які змінні можливо створювати
# 1) Змінні завжди повинні писатись маленькими буквами
# 2) Змінні повинні завжди починатися з алфавитних символів.
# Правильно: name, age, name, name2, number, n1 n2
# Неправильно: !name, 1name, 2name

# Як створити змінні з двух слів
# В данних випадках використовуються символ "_"
# Приклад:
# student_name - "Asel", user password="sdkfj12412"
# number_1, number_2



# Строка

# Строка = це стандартний тип данних в Python
# Означає текстовий формат данних
# Будь який текст і порядок символів, який розміщений в 
# "", '' рахується строкою

first_name = "John"
last_name = "Jackson"

# print("Hello", first_name)
# #форматування строк
# print(f"My name is {first_name}")

# #Конкантенація - з'єднання строк з допомогою "+"

# full_name = first_name + " " + last_name
# # Пробіл рахується символом
# print(full_name)

#Приклад конкантенації
# text = "I am" + " 10 years old"
# print(text)
# world = "A" + "p" + "p" + "l" + "e"
# print(world)

# методи строк
# Це спеціальні команди для строк, які
# допомагають взаємодіяти з строками і якось з ними працювати

# name = "asel"
# print(name.title())
# # title = Це метод, який робить пкрший символ строки заглавним
# text = "i am smith"
# print(text.title())
# Особливість title - він робить всі слова в строці заглавними

# capitalize - робить тільки перший символ строки заглавною
# text = "i am smith"
# print(text.capitalize())

# lower, upper - меттоди строк
# text = "abc"
# print(text.upper())
# name = "Anton"
# print(name.upper())
# text2 = "abc24"
# print(text2.upper())
# Меттод upper - робить всі маленькі алфавітні символи заглавними буквами

# text = "ABC"
# print(text.lower())
# name = 'aNTon'
# print(name.lower())
#  метод lower - робить ісі заглавні букви строки маленькими
# Сенс методу редагування строк, отримання інформації про строку,
# взаємодія з строкою.

# Функція input()
# name = input("Please, enter your name: ")
# # input() =це системна функція, яка створює можливість
# # вносити інформацію із консолі (терміналу)
# print(f"Hello, {name}")

# number1 = int(input("Please, enter first number: "))
# number2 = int(input("Please, enter second number: "))
# print(number1)
# print(number2)
# print(10+20)
# input вводить всі дані в форматі строки (string)
# print(number1+number2)
# * - множення, / - ділення, - (різниця)
# print(number1*number2)
# print(number1/number2)
# print(number1-number2)

# метод строк - count ()
text = "Apple"
# # print(text.count("a"))
# text2 = "lalala "
# print(text2.count ("a "))
