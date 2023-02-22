# Тема:
# Перебір списків.
# Цикл for

# Цикл for - це команда для створення циклу
# із перебераючих обєктів в python
# Важливо! Цикл for являється кінцевим.

# Перебираючи обєкти - це обєкти, які дозволяють
# циклу пройтись по його елементам
# По англійсткі перебираючи обєкти називаються - 
# ITERABLE OBJECTS

# ЦИкл for повторюється таку кількість раз, яку кількість елементів знаходиться 
# в списку.
# names = ["smith", "john", "askar", "anna"]
# for name in names:
#     print(f"My name is {name.capitalize()}")

    # Ітерація - це одне повторення кода в циклу
    # Ітерація - це синонім слова перебір
    # Зацікавлений обєкт - це той обєкт над яким проводиться перебір.
    # Інтератоор - це комаг=нда, яка проводить перебір.

# Табуляція - це отступи для створення блоку коду в Python
# Блок коду  - це окремо розділена зона коду.

# for *перебір*:
    # блок коду для циклу for
    # тіло циклу.


# names = ["Smith", "John", "Askar", "Anna"]
# for name in names:
#     result = name.upper()
#     print(result)
#     print("HELLO")

# print("WORLD")
# Звстереження 1
# Код після циклу котрий знаходиться поза тіла циклу, буде виконаний
# тільки після закінчення повного цикла роботи

# Застереження 2
#  Код, який знаходиться в середині тіла циклу повториться стільки, скільки
# сам цикл.

# numbers = [10,12,15,20,5,6,10]
# Завдання: Знайти множення всіх чисел в даному списку.

# result = 1
# for n in numbers:
#     result = result * n
# print(f"Результат: {result}")

# result = 0
# for n in numbers:
#     result = result + n
# print(f"Результат: {result}")


# Завдання:
# Акилай вирішила запросити свохз друзів на день народження.
# В нех є список друзів.
friends = ["aya", "anna", "asel", "saltanat"]
# Допоможіть порахувати скільки потрібно шматочків торту для гостей.
# Якщо одному гостю потрібно 2.25 шматочка. Потрібно порахувати також саму Акилай.

# Також допоможіть створити запрошення для кожного гостя окремо.
# Використовуючи цикл for/
# Приклад:
# Дорога, Anna. Запрошую тебе на моє ДР.

# Скількі шматочків потрібно для кожного гостя.

number = len(friends)+1
print(f"Всього шматочків потрібно для гостей: {number*2.25}")

# Запрошення.

for f in friends:
    print(f"Дорога, {f.capitalize()} Запрошую тебе на моє ДР.")

#  Завдання: 
#  Є список чисел.
nambers = [2,4,6,8,10,12,14,16]

# Знайти квадрати та куби ціх чисел і вивести на екран
# Приклад: Квадрат числа 2 = 4, Куб числа 2 дорівнює 8 