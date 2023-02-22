# Тема: Команда if.

# if умова:
    # тіло умови.

# Тіло умови виконуюється або активується тільки якщо
# умова правильна.

# Для правельності уови команда if повинна отримати у вілповідь True
# Команда if <---=True із < умова


# product = "banana"

# if product == "apple":
#     print("Це яблуко")

# == - це оператор порівняння для порівняння двух значень
# зліва і спрва. Якщо вони рівні, оператор поветає True,
# В іншому випадку повертається False.

# print(5==3) # Виводить: True

# names = ["Luiza", "Askar", "JoHn", "JohN"]
# for n in names:
#     if n.lower() == "john":
#         print(n.upper())

# password = "qwerty123"
# user_password = input("Введіть ваш пароль: ")
# # використовужмо strip() для видалення лишніх пробілів з боків.
# if user_password.strip() == password:
#     print("Ваші дані вірні, ви усмішно авторизувались")

# Оператор нерівності - "!="
# Оператор нерівності перевіряє , що значення зліва та справа нерівні.
# Якщо це так повертає True, в іншому випадку False

# product = "mushrooms"
# if product != "cheese":
#     print("Ваш продукт в наявності")

# user_status = "banned"

# if user_status != "active":
#     print("Ваш акаунт забенений!")

# Оператори меньше(<), більше(>), менше рівно(<=) і більше рівно(>=)

# age = int(input("Введіть ваш вік: "))

# if age > 16:
#     print("Ви можете зайти в цей заклад")
# else:
#     print("Вам вхід заборонений")

# else - це команда для випадку не виконання умови if.
# else зпрацьовує тільки, якщо не спрацював if.
# Важливо! if і else не можуть відпрацювати одночасно в одній конструкції


# Оператор "in"
# Даний оператор перевіряє, що один обєкт зліва присутній в іншому обєкті справа
# Наприклад:
# "a" in "apple" # Виводить: True
# Також ми можемо перевірити наявність одного елемента в іншому списку.

# banned_users = ["kg_boy", "aika98", "zloibala", "patriot"]
# username = input("Введіть ваш логін: ")

# if username in banned_users:
#     print("Ваш аккаунт в бані")
# else:
#     print("Ви успішно увійшли!")

# Переьбір срисків та створення умови
# new_users = ["natlus", "kg_boy", "alkash", "alina98"]

# taken_users = ["kg_boy", "alkash", "patriot", "lena97"]

# active_users = []

# for new_user in new_users:
#     if new_user in taken_users:
#         print(f"Логін {new_user} зайнятий, спробуйте ще раз!")
#     else:
#         active_users.append(new_user)
#         print(f"Ваш аккаунт під логіном {new_user} успішно створено!")
# print(active_users)

# Завдання:
# Існує два списку чисел і один пустий список.
# Добавте в третій пустий список тількі ті числа із першого списка
# які відсутні і другому.
# numbers1 = [2,4,6,10,12,14,17]
# numbers2 = [4,6,12,15,17,18]
# numbers3 = []

# for n1 in numbers1:
#     if n1 in numbers2:
#         print(f"Чила {n1} присутні в списку numbers1 та nambers2")
#     else:
#         numbers3.append(n1)
#         print(f"Додані до списку numbers3 числа {n1}")
# print(numbers1)
# print(numbers2)
# print(numbers3)

# В кінці прінт всіх трьох списків

# Завдання 2:
# Існує дві групи А та В группа. Існує визначений список студентів.
# Потрібно відсортувати студентів по групам.
# students = ["Aktan-group-b", "Luiza-group-a", "John-group-b", "Askar-group-a"]
# group_b = []
# group_a = []

# for s in students:
#     if "group-a" in s:
#         group_a.append(s)
#     else:
#         group_b.append(s)
# print(group_a)
# print(group_b)

# Завдання 3:
# Користувач вводить через input свій логін. Перевірте, що його немає в списку
# уже створених логінів, щоб не створювати копії.
# Якщо данний логін зайнятий, напишить про це користувачу
# Якщо логін вільний, добавте його в список логінів

# usernames_list = ["patriot", "killer_kg", "natlus", "alina98", "spaceof.heat"]
# username = input("Введіть ваш логін: ")


 if username in usernames_list:
     print(f"Ваш логін {username} зайнято, спробуйте інший!")
 else:
     usernames_list.append(username)
 print(usernames_list)

