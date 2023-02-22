# class A:
#     def __init__(self, type):
#         self.type = type
#
#     def get_name(self):
#         print("A класс")
#
#
# class B(A):
#
#     # метод overwrite - переписання методу в успадкованому класі
#     def get_name(self):
#         print("B class")

# Множинне наслідування.
# MRO - method resolution order

# class A:
#
#     def move(self):
#         print("Method from A")
#
#
# class B:
#
#     def move(self):
#         print("Method from B")
#
#
# class C(B):
#     pass
#
#
# class D(A, C,):
#     pass
#
#
# print(D.mro())
# d = D()
# d.move()

# #  Багаторівневе наслідування.
# class Grandfather:
#
#     def __init__(self, name):
#         self.name = name
#         self.eyes_color = "brown"
#
#
# class Father(Grandfather):
#
#     def __init__(self, name):
#         super().__init__(name)
#         self.eyes_color = "green"
#
#
# class Son(Father):
#
#     def __init__(self, name):
#         super().__init__(name)
#         self.eyes_color = "blue"
#
#
# son = Son("Alex")
# print(son.eyes_color)
# # True
# print(isinstance(son, Son))
# # True
# print(isinstance(son, Father))
# # True
# print(isinstance(son, Grandfather))
# # У випадку наслідуванні, всі батьківські класи являються класами об'єкта


# class A1:
#
#     def get_info(self):
#         print("Hello from class A1")
#
#
# class A2(A1):
#     pass
#
#
# class B1:
#     def get_info(self):
#         print("Hello from class B1")
#
#
# class B2(B1):
#     pass
#
#
# class C(A2, B2):
#     pass
#
#
# c = C()
# c.get_info()
# print(C.mro())

# Завдання: Класс Alphabet
# 1) Створіть клас Alphabet
# 2) Створіть метод init(), всередині якого будуть визначено дві динамічні властивості
#         1. lang - мова
#         2. letters - список букв
# Початкові значення властивостей беруться із вхідних параметрів методу.
# 3. Створіть метод print(), який виводить в консоль букви алфавіту
# 4. Створіть метод letters_num(), який поверне кількість букв алфавіту

# Класс EngAlphabet
# 1) Створіть класс EngAlphabet шляхом наслідуванням від классу Alphabet
# 2) Створіть метод init(), всередині якого буде викликатися батьківський метод init(). В якості параметрів
# йому будуть передаватись позначення мови (наприклад 'En') і строка, що складається із всіх букв алфавіту.
# 3) Додайте приватну властивість _letters_num, яка буде зберігати кількість букв в алфавіті
# 4) Створіть метод is_en_letter(), яка буде приймати букву в якості параметра і визначати, чи відноситься буква
# до англійського алфавіту.
# 5) Пере визначте метод letters_num() - нехай в наявному класі він буде повертати значення властивості _letters_num.
# 6) Створіть метод example(), який буде повертати приклад тексту англійською мовою.

# Тести:
# 1) Створіть об'єкт класу EngAlphabet
# 2) Надрукуйте букви алфавіту для цього алфавіту
# 3) Виведіть кількість букв в алфавіті
# 4) Перевірте, відноситься буква F до англійської мови
# 5) Перевірте, відноситься буква Щ до англійської мови
# 6) виведіть приклад тексту англійською мовою
# 20:40 старт

# class Alphabet:
#
#     def __init__(self, lang, letters):
#         self.lang = lang
#         self.letters = letters
#
#     def alphabet(self):
#         print(self.letters)
#
#     def letters_num(self):
#         print(len(self.letters))
#
#
# class EngAlphabet(Alphabet):
#
#     def __init__(self, lang, letters):
#         super().__init__(lang, letters)
#         self.lang = "En"
#         self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
#                         "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
#                         "W", "X", "Y", "Z"]
#
#     def is_en_letters(self):
#         input_letter = input("Введіть літеру для перевірки: ")
#         if input_letter.upper() not in self.letters:
#             print("Літера не являється англійською")
#         else:
#             print("Літера англійського алфавіту")
#
#     def __letters_num(self):
#         letters_num = len(self.letters)
#
#     # def letters_num(self):
#     #     pass
#
#     def example(self):
#         print("Приклад тексту Англійською мовою: An example of a test in English")
#
#
# eng = EngAlphabet("en", "B")
# eng.alphabet()
# eng.letters_num()
# eng.is_en_letters()
# eng.example()
