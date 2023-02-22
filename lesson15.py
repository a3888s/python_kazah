# Тема: Словники(Dictionary)- dict

# Структура словника:
# {} - словник міститься між фігурними скобками
# {"name":"Askar"} - зберігаються дані в вигляді пар ключів і значень.
# {"first_name":"John", "last_name", "Smith"} - Словник може
# зберігати необмежену кількість пар (ключів та значень)

# Приклад використання:

alien = {"color": "red", "points": 10}

# # отримання інформації
# print(alien_0 ["color"])
# print(alien_0 ["points"])

# Додавання нових пар ключів і значень
alien["x_position"] = 0
alien["y_position"] = 10

print(alien)

# Зміна даних в словнику

# alien_0 = {"color":"red", "points":10}
# alien_0["color"] = "blue"
# # alien_0["points"] = alien_0["points"] + 10
# alien_0["points"] += 10
# print(alien_0)

# x = int(input("Enter x position: "))
# alien_0["x_position"] = x
# print(alien_0)

# Завдання:
# user_date = {"username":"patriot", "password":"qwerty123"}

# user_name = input("Введіть ваш нік нейм: ")
# if user_name == user_date["username"]:
#     user_food = int(input("Ви дійсно хочете змінити пароль?, Змінити пароль - 1, Залишити - 2: "))
#     if user_food == 1:
#         new_user_password = input("Введіть ваш новий пароль: ")
#         user_date["password"] = new_user_password
#         print("Ваш пароль зміненно!")
#         print(user_date)
#     else:
#         print("Ваш пароль не було змінено")
# else:
#     print("Такий користувач відсутній!")

# Видалення пар ключ: значення із словника
# alien_0 = {"color":"red", "points":5, "z_posituon":10}
# # Видалення через ключ.
# del alien_0["z_posituon"]
# print(alien_0)


# Робота зі словником.

# user_data = {"frist_name":"John",
#             "last_name":"Smith",
#             "email":"smith@gmail.com",
#             }
# text = f"My fullname is {user_data['frist_name']} {user_data['last_name']}"
# print(text)

# aliens = [
#     {"name":"mark", "color":"red"},
#     {"name":"alica", "color":"green"},
#     {"name":"john", "color":"green"},
#     {"name":"alan", "color":"red"},
#     ]
# reds = []
# greens = []

# for a in aliens:
#     if a["color"] == "red":
#         reds.append(a)
#     elif a ["color"] == "green":
#         greens.append(a)
# print(reds)
# print(greens) 


# Завдання:
# Існує список користувачів:
# users = [
#     {"username":"killer90", "is_active":True},
#     {"username":"patriot", "is_active":False},
#     {"username":"osmanov979", "is_active":True},
#     {"username":"smith_john", "is_active":True},
#     {"username":"alina77", "is_active":False},
# ]

# active_user = []
# noactive_users = []

# for u in users:
#     if u["is_active"] == True:
#         active_user.append(u)
#     else:
#         noactive_users.append(u)
# print(active_user)
# print(noactive_users)

# Методи слоників.
# метод .get() - отримання значень через ключ

# alien_0 = {"position":10}
# # print(alien_0["color"])
# # через даний метод, існує ризик виклику помилки KeyError
# # Якщо такого ключа немає в словнику
# # Якщо ви не знаєте існуж такий ключ чи ні.
# # Щоб забезпечити себе від помилки, використовужмо метод . get()
# print(alien_0.get("color"))

# user = {"username":"alan22", "first_name":"Alan"}
# print(user.get("first_name", "Пусте імя"))

# Метод .update()

alien_o = {"color": "red", "points": 10}
position = {"x_position": 10, "y_position": 5}
alien_o.update(position)
print(alien_o)

