# Тема: Методи строкта тип данних список

# replace - метод строк, 
# який замінює частину строки на іншу строку

# product = "Aple"
# product = product.replace("p", "pp") #перезберігання в ту де змінну
# print(product)

# Видалення зайвиз символів.
# name = "Asia-Mall"
# name = name.replace("-", " ") # Змінюємо символ на інші символи.
# print(name)

# Зміна цілих слів в строці

# text = "Fotball is my favorite sport"
# text = text.replace("Fotball", "Basketball")
# print(text)

# Зміна декількох символів в строці

# text  = "my-name-is-john"
# text = text.replace("-", " ")
# text = text.replace("-", " ",2) #Третій параметр, який передається в replace.
# це кількість змін в даній строці через replace
# print(text)

#  Метод strip() видаляє зайві символи з двух країв строки.
# За замовчуванням видаляє лише пробіли

# name = input("Enter tour name: ")
# name = name.strip()
# print(f"Hello, {name}")

# Видалення інших символів через strip()
# strip - видаляє символи з двух країв строки
# text = "--Hello--World--"
# text = text.strip("-")
# print(text)

# Метод строк можливо застосувати в ряд
# text = "!hello-world!"
# text = text.strip("!").replace("-", " ").upper()
# print(text)

# Функція len() - повертає кількість символів в строці

# text = "A"
# print(len(text))
# text = "John"
# result = len(text)
# print(result)

# name1 = input("Enter first name: ")
# name2 = input("Enter second name: ")
# result = len(name1)+len(name2)
# print(f"Two names length: {result}")

# ТЕМА: Тип данних список(list)

# Коли створюється змінна для списку, змінна повинна бути в множ.числі
# products = ["milk", "bread", "apple", "oranje juice"]

#  Індексація в списках виникає  при кожному елементі.
#  Елемент списку - це один обєкт поміщенний в список і
# розділений від іншиз комою.

# print(products[1])
# print(products[3])
# print(products[2].upper())
# Якщо елемент списку являється строкою,
# ми можемо застосувати до цього елементу його метод.


# names = ["John", "katya", "Askar"]
# text = f"My name is {names[0]}"
# print(text)
# text2 = "I am " + names[1].title()
# print(text2)

# Список з числами
# numbers = [10,15,20,5,60]
# print(numbers[0]+numbers[-1])

#  Зміна елементів в списку.
# products = ["milk", "coffee", "juice", "melon"]
# products[1] = "tea"
# # Звертається до індексу і вказав нові значення
# # ми можемо змінити елемент на нові значення.
# print(products)


# Додавання елементів в список.

# products = ["milk," "tea", "orange"]
# products.append("bread") # додавання нового елемента
# print(products)
# Метод append()- це метод строк, який добавляє новий елемент в список
# Додавання виникає в кінці списку.

# Видалення елементу із списку через індекс.

# products = ["milk", "orange", "coffee", "tea", "juice"]
# del products[3]
# print(products)

# del 

# Завдання 1

# Завдання 2

# Завдання 3

