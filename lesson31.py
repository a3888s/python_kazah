# Принципи ООП.
# Існує чотири принципа ООП.
# 1) Наслідування
# 2) Інкапсуляція
# 3) Поліморфізм
# 4) Абстракція

# Наслідування в ООП.

# class A:
#
#     def __init__(self):
#         self.name = "CLASS A"
#
#     def get_something(self):
#         print("I am method from class A")


# class A - це батьківський класс від якого наслідується class B
# class B - це субкласс(підклас), який наслідує все від class A
# class B(A):
#     pass
#
#
# b = B()
# b.get_something()
# print(b.name)
# print(isinstance(b, A))
# print(isinstance(b, B))

# Існує декілька видів наслідування:
# 1) Множинне наслідування
# 2) Багаторівневе наслідування


# Приклад багаторівневого наслідування:
# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# class C(B):
#     pass


# Приклади на множинні наслідування
# class A:
#     pass
#
#
# class B:
#     pass
#
#
# class C:
#     pass
#
#
# class D(A, B, C):
#     pass

# Приклади:
# class Animal:
#
#     def get_noise(self):
#         print("aРРРР")
#
#     def move(self):
#         pass
#
#
# class Cat(Animal):
#
#     # Ми взяли батьківський метод з Animal і переоприділили його під себе.
#     def get_noise(self):
#         print("мяу мяу")
#
#     def move(self):
#         print("Ходить на 4 лапах...")
#
#
# cat = Cat()
# cat.get_noise()
#
#
# class Bird(Animal):
#
#     def get_noise(self):
#         print("чірик чірик")
#
#     def move(self):
#         print("Літає")
#
#
# bird = Bird()
# bird.get_noise()

# class Human:
#
#     def __init__(self, name, age, type):
#         self.name = name
#         self.age = age
#         self.type = type
#
#     def say(self):
#         print("Говорить...")
#
#     def move(self):
#         print("Рухається")
#
#
# class Child(Human):
#
#     def say(self):
#         print("Кричить... ААААААААААА.....")
#
#     def move(self):
#         print("Повзає...")
#
#     def play(self):
#         print("Грає в іграшками")
#
#
# class Adult(Human):
#
#     def __init__(self, name, age, type, cash, salary, is_married):
#         super().__init__(name, age, type)
#         self.cash = cash
#         self.salary = salary
#         self.is_married = is_married
#
#     def say(self):
#         print(f"Привіт, мене звати {self.name}")
#
#     def move(self):
#         print("Ходить на двух ногах")
#
#     def earn(self):
#         self.cash += self.salary
#         print(f"Ваш наявний рахунок: {self.cash}")
#
#
# adult = Adult("Askar", 30, "M", 10_000, 30_000, False)
# adult.earn()
# adult.say()
#
# child = Child("Osmon", 1, "M")
# child.say()
# child.play()

# Завдання:
# Створіть класс OldHuman(), який наслідується від классу Human
# Додайте додаткові властивості типу пенсія, кількість внуків
# Додайте метод get_pension(), який отримує пенсію і додайте у свій cash
# Переопреділіть методи із Human say, move.

# class Human:
#
#     def __init__(self, name, age, cash):
#         self.name = name
#         self.age = age
#         self.cash = cash
#
#     def say(self):
#         print(f"Я {self.name}, працюю")
#
#     def muv(self):
#         print("Іду сьогодні на роботу")
#
#
# class OldHuman(Human):
#
#     def __init__(self, name, age, cash, pension, grandson):
#         super().__init__(name, age, cash)
#         self.pension = pension
#         self.grandson = grandson
#
#     def get_pension(self):
#         self.cash += self.pension
#         print(f"Нарахована пенсії {self.pension}")
#         print(f"Всього накопичено {self.cash}")
#
#     def say(self):
#         print(f"Я {self.name}, пенсіонер")
#
#     def muv(self):
#         print(f"Іду сьогодні до внуків, їх у мене {self.grandson}")
#
#
# human = Human("A3888S", 30, 25000)
# human.say()
# human.muv()
# oldhuman = OldHuman("Petro", 65, 100_000, 15_000, 4)
# oldhuman.say()
# oldhuman.muv()
# oldhuman.get_pension()

# ДЗ
# Існує класс Professor().
# Професор має властивості імя, напрямок та список студентів, яких він навчає.
# Існує класс Students(), який має ім'я список професорів, на чиї лекції ходять студенти
# Студент може записатись на курс профессора(subscribe_professor). Тоді професор повинен додати в список студента.
# А студент до списку студентів професора.
# Студент може відписатись від курса професора(unsubscribe_professor). Тоді ми повинні видалити професора зі списку
# студента і студента зі списку професора.
# Ми можемо дізнатися список студентів, які ходять до професора
# Ми можемо дізнатися список професорів, на які записаний студент


# class Professor:
#
#     def __init__(self, items, professor_name):
#         self.items = items
#         self.professor_name = professor_name
#         self.students_list = []
#
#
# class Students(Professor):
#
#     def __init__(self, items, professor_name, student_name):
#         super().__init__(items, professor_name)
#         self.student_name = student_name
#         self.professor_list = []
#
#     def subscribe_professor(self):
#         self.professor_list.append(self.professor_name)
#         self.students_list.append(self.student_name)
#
#     def unsubscribe_professor(self):
#         self.professor_list.remove(self.professor_name)
#         self.students_list.remove(self.student_name)
#
#
# olexandr = Students("Фізика", "Професор Іван", "Студент Олександр")
# vasyl = Students("Математика", "Професор Іван", "Студент Василь")
#
# olexandr.subscribe_professor()
# vasyl.subscribe_professor()
# # vasyl.unsubscribe_professor()
# print(vasyl.professor_list)
# print(olexandr.professor_list)
# print(olexandr.students_list)
















