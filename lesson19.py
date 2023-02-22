# Тема: Робота з файлами.

#  функция open() робить можливим читання файлів

# file = open("test.txt", encoding="utf-8")
# text = file.read().strip()
# # read()- спеціальний метод, який читає файл
# # та повертає строку.

# print(text)

# Режим запису вказується через "w"
# file = open("test.txt","w", encoding="utf-8")
# text = "New text fom python file"
# file.write(text)

# Режим - "w" створює текствий файд, якщо його не існує.
# даний файл перезапише там все поновому.

# Режим запису "a" - append
# В режимі "a" - діні файлу не видаляються під час запису.
# Нові дані додаються в кінці файлу.
# file = open("students.txt","a", encoding="utf-8")

# first_name = "Askar"
# last_name = "Osmonov"
# age = 20

# text = f"{first_name} {last_name}-{age} \n"
# # \n - це спуск на нову строку в файлах чи текстових форматах.
# file.write(text)


# file = open("students.txt","a", encoding="utf-8")
# active = True
# while active:
#     first_name = input ("Введіть ваше імя: ")
#     mark = input("Введіть вашу оцінку: ")
#     file.write(f"{first_name}-{mark} \n")
#     massage = input("Якщо бажаєте вийти із програми, напишіть quit: ")
#     if massage == "quit":
#         active=False


# Завдання 1 
# Прочитайте текст в файлі test.txt. Видаліть лишні пробіли з двух сторін.
# Після порахуйте кількість символів в даній строці.
# Порахуйте кількість символу "," в даному тексті.

# file = open("test.txt", encoding="utf-8")
# text = file.read().strip()
# print(text)
# print(f"Кількість символів: {len(text)}")
# znak = []
# for t in text:
#     if t == ",":
#         znak.append(t)
# print(f"Кільксть знаків ',': {len(znak)}")

# Метод readlines()
# Метод close()
# file = open("students.txt", "r", encoding="utf-8")
# lines = file.readlines()
# print(lines)
# for l in lines:
#     l = l.strip()
#     print(l.upper())
# file.close()
# # метод close - закриває файл


# Vtnjl readline()

# file = open("students.txt", "r", encoding="utf-8")
# line = file.readline().strip()
# print("1", line)
# line = file.readline().strip()
# print("2", line)

# приклад використання readline:
# file = open("students.txt", "r", encoding="utf-8")
# while True:
#     l = file.readline().strip()
#     if not l:
#         break
#     print(l)
# file.close()