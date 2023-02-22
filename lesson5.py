# Робо зі спискаи та методами списка

# insert() - метод списка, який вставляє новий елемент в потріьний індекс

# names = ["Almaz", "Arthur", "Bektur", "Elmar", "Eldana"]
# names.insert(2, "Anna")
# # Елементи замість, якиї вставляється новий елемент здвигається в право і кожен
# # елемент отримує новий індекс.
# print(names)

# Видалення елементів по значенню.
# remove() - метод списку, який видаляє елементи із списку по яго значенню

# products = ["milk", "banana", "bread", "chips"]
# products.remove("banana") # Пишемо значення елемента, який хочемо видалити.
#  Регістр букв повинні сходитись при видаленні через remove.
# products.remove("juice")
# Видалення через remove викликає помилку.
# print(products)


# names = ["Ali", "John", "Vera", "Ali"]
# names.remove("Ali") # пробуємо видалити всі значення Ali.
# При наявності деклькох схожих значень в списку.
# метод remove видалить тільки самий перший,  котрий він зустріне в списку вна початку.
# print(names)

# В даній задачі видаляємо елементи із списку, запитав їх у користувача:
# Щоб привести дані в один формат, використовуючи метод строк.
# products = ["coffee", "meat-1kg", "coca-cola", "sugar"]
# print("Список продуктов: ", products)
# name = input("Введіть назву продукту для видалення: ")
# name = name.strip().lower()
# products.remove(name)
# print(products)

#  count() - метод списку, повертає кількість елементів з схожим елементом
# lessons = ["алгебра", "література", "фізра", "Алгебра", "алгебра"]

# mah_count = lessons.count("алгебра")
# print(mah_count)  # 3
# print(lessons.count("фізра")) # 1
# print(lessons.count("Хімія")) # 0

# numbers = [10, 10, 0, 10, 0, 5, 10, 0]
# print(numbers.count(10)) # 4

# .index() - метод строк, котрий повертає значення в списку

# alphabet = ["a", "b", "c", "d", "e", "a"]
# latter_index = alphabet.index("a")
# print(latter_index)
# Метод індекс повертає індекс тільки самого першого елемента, 
# котрий підходить під його пошук

# Для позначення початку та кінця пошуку через index використовуємо слід. парметри
# /index(*vaiue*, start_index, end_index)
# *value* - значення для пошуку в списку
# start_index - індекс з якого починається пошук
# end_index - до якогоробиться пошук значення
# print(alphabet.index("a", 1))
# print(alphabet.index("a", 1,6)) # Вказуємо зону пошуку

# Метод .sort - сортує срисок по визначеному списку

# alphabet = ["z", "y", "a", "p", "o", "b", "e"]
# alphabet.sort()
# print(alphabet)
# sort () - сортує строки і символи алфавіту по алфавіту чи номеру.
#  Номер символу ми можемо дізнатись через функцію adr().

# words = ["abd", "abc", "adk", "aez", "aea"]
# words.sort()
# print(words)
# Якщо символи в елементах схожі, то sort() бере слідуючий сисмвол і так дальше
# поки не знайде символ, якисй відрізняеться.

# names =["Zalkar", "Kiril", "Almaz", "Bermet", "Elena", "Azat"]
# names.sort()
# print(names)

# words = ["computer", "Computer", "Airbus", "airbus", "book", "Book", "Zebra"]
# words.sort()
# print(words)
# Букви чи символи алфавіту сортуються в залежності від регістра букв(від розміру)
# Першим завжди являється більші букви, після ідуть маленькі.

# Причина:
# В системі символів символ "А" - має номер 65.
# Символ "а" - має номер 97.
# Це можливо дізнатися через функцію odr()

# Завдання:
#  В наявності список оцінок. В якому є оцінки студентів за навчальний рік.
# marks = [2,3,2,4,5,5,5,5,4,2,4,3,2,5]
# Потрібно знайти кількість кожної оцінки в цьому списку.
# Також потрібно знайти середню оцінку в даному списку.
# Потрібно знайти також вілсоток кожної оцінки.

#  Сумa чисел  в списку.
# sum() - дана функція заходить сумму всіх чисел в списку.
# numbers =[100, 200, 500, 200]
# result = sum(numbers)
# print(result)

# ДЗ
# Дано:
marks = [2,3,2,4,5,5,5,5,4,2,4,3,2,5]

# 1. Знайти кількість кожної оцінки в цьому списку.

print("1. Кількість оцінок в списку:")
print("Оцінок 2 -", marks.count(2), ", Оцінок 3 -", marks.count(3), ", Оцінок 4 -", marks.count(4)
, ", Оцінок 5 -", marks.count(5))

# 2. Знайти середню оцінку в даному списку.

sum_marks = sum(marks)/len(marks)
print(f"2. Середня оцінка списку: {sum_marks}")

# 3. знайти відсоток кожної оцінки

# общее кол. - 100%
# кол. оценки - Х
# формула: х = (100% * кол.оценок)/общее кол.

five_procent = 100*marks.count(2)/len(marks)
print(f"3.Відсоток оцінки 2: {five_procent}")

five_procent = 100*marks.count(3)/len(marks)
print(f"3.1 Відсоток оцінки 3: {five_procent}")

five_procent = 100*marks.count(4)/len(marks)
print(f"3.2 Відсоток оцінки 4: {five_procent}")

five_procent = 100*marks.count(5)/len(marks)
print(f"3.3 Відсоток оцінки 5: {five_procent}")