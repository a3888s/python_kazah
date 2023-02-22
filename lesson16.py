# Робота зі словнками.

# Зберігання складних структур в словниках.

# user_date = {
#     "username":"Alan22",
#     "age": 25,
#     "hobbies": ["Спорт", "Читання", "Малювання", "Танці"],
#     "education" : {
#         "uni": "КГТУ",
#         "faculty":"Інформатика",
#         "is_finished":False,
#         "gpa": 3.9
#         }
# }

# # Отримання списку із словника.

# print(user_date.get("hobbies"))
# for h in user_date.get("hobbies"):
#     print(h, end="-")


# Отримання данних словника в середині іншого словника.

# print(f"Університет: {user_date['education']['uni']}")

# if user_date["education"]["is_finished"]:
#     print("Закінчив університет")
# else:
#     print("Навчається")

# students = [
#     {
#     "name":"Alan",
#     "education":{"faculty":"A1", "is_finished":True},
#     "marks":[2.4,3.7,4.0,3.4,4.0,3.5]
#     },
#     {
#     "name":"Venera",
#     "education":{"faculty":"A1", "is_finished":False},
#     "marks":[3.0,3.5,3.9,3.1,2.9,3.1]
#     }
# ]
# Завдання.
# Знайдіть студентів котрі завершили навчання.
# Перемістьть їх в окремий список
# Найдіть середній бал кожного студента по їх оцінках.
# Та додайте їх в словник

# graduets = []
# for s in students:
#     if s["education"]["is_finished"]:
#         graduets.append(s)
#         print(f"Завершили навчання: {graduets}")
#     sum_marks = (sum(s["marks"])/len(s["marks"]))
#     s["gpa"] = sum_marks
#     print(f"Середня оцінка студента: {s['name']} - {s['gpa']} бали")