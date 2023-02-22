# Рішення ДЗ1
# Ви отримуєте порядок чисел розділених через кому із допомогою
# функції input.
# Створіть список із цих чисел введених через функцію.
# Найдіть їх сумму і квадрат цих чисел.


# text = input("Введіть через кому: ")
# numbers = text.split(",")
# numbers_int = []
# squaers = []
# for n in numbers:
#     n_int = int(n)
#     numbers_int.append(n_int)
#     squaers.append(n_int**2)

# print(sum(numbers_int))
# print(squaers)

# Рішення ДЗ2
# Професор в спису проставив всім студентам оцінки.
students_marks = [
    "Askar-4.7",
    "Arman-3.8",
    "Anna-4.2",
    "Aya-5.0",
    "John-2.5",
    "Luiza-4.9"    
]
# # Завдання вашої програми знайти середній бал даної групи студентів.
# # Додаткове завдання.
# # Вивидіть на екран най більший макисмальний і мінімальний в групі без імені.
mark_float = []
for student in students_marks:
    s = student.split("-")
    mark = float(s[1])
    mark_float.append(mark)
sum_mark = sum(mark_float)/len(mark_float)
sum_mark = round(sum_mark, 1)
print(sum_mark)
print(max(mark_float))
print(min(mark_float))