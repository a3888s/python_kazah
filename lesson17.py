# Тема: Цикл While.

# x=0
# while x < 10:
#     print(x)
#     x +=1

# print(x)
# Цикл буде продовжуватись поки "x" не стане більше 9.
# Після не виконується умова циклу і цикл зупигяється.

# print("Введіть повідомлення, я повторю його!")
# massage = ""
# while massage != "quit":
#     massage = input("Введіть текс: ")
#     print(massage)

# While цикл буде працювати і продовжувати цикл поки massage не рівний quit.
# Як тільки користувач введе "quit" цикл while зупиниться.
# Тому що умова "massage" != "quit".

# поки massage не рівний "quit" умова буде повертати True

# Видалення із списку через цикл While.
# Вилдаляє всі apple

# products = [
#     "apple",
#     "milk",
#     "apple"
#     "coffe",
#     "apple",
# ]
# while "apple" in products:
#     products.remove("apple")

# print(products)

# Видаляємо лишні значення apple і залишаємо один.
# products = [
#     "apple",
#     "milk",
#     "apple"
#     "coffe",
#     "apple",
# ]
# while products.count("apple")>1:
#     products.remove("apple")

# print(products)

# Прапорці в умовах While.

# active = True

# while active:
#     print("Для вихлду із програми, напигшіть quit.")
#     massage = input("Введіть текст для повторення: ")
#     if massage == "quit": 
#         # точка виходу із циклу через флаг
#         active=False
#     print(massage)

# Команда Break в циклі While.
# Дана команда зупиняє цикл на тому місці, де визивається break.
# Подальший код всередині після break вже не виконається і цикл завершиться.

# while True:
#     massega = input("Введіть текст для повтору: ")
#     if massega == "exit":
#         break
#     print("Це принт після умови")


# active = True
# while active:
#     massega = input("Введіть текст для повтору: ")
#     if massega == "exit":
#         active = False
#     print("Це принт після умови")


# continue в циклі while
# Через дану команду "continue" ми можемо переривати один із кругів циклу
# без його повної зупинки.
# Тобто при якихось умовах цикл буде перириваться та починатись
# з нового круга.

# Задача - 1
# Існує текст з великими та маленькими символами.
# Ваше завдання з домопомогою циклу while видалити всі велиуі символи,
# поки не залишуться тільки маленьі символи.
# test = "ФприЙЦККЦЙКвЧСМЯЧМеЖДДЛт"

# even_numbers = []
# x = 1
# while x < 100:
#     x +=1
#     if x % 2 != 0:
#         continue
#     even_numbers.append(x)
    
# print(even_numbers)

# Завдання 2
# Існує список користувачів, яким дозволений вхід на сайт.
# Запитуйте у користувача його username в циклі.
# Продовжуйте цикл поки користувач не введе username із списку
# Після успішного вводу username, привітайте та зупиніть цикл
# Якщо він ввів неправильний username, то повідомте, що він не може увійти на сайт

# username = ["alina91", "ata22", "patriot2002", "kg_bishkek1"]
# active = True
# while active:
#     user = input("Введіть Ваш  username: ")
#     if user in username:
#         print("Ви ввели вірний username")
#         active = False
#     else:
#         print("Ви ввели не вірний username! Спробуйте ще")
