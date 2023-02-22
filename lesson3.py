# Тема: Зрізи строк

# Строка [start:end:step] - формат роботи зрізу через індекс

numbers = "0123456789"
text = "ABCDEFGHLMN"

# Стандартні значення під час зрізу

# print(numbers[3:]) - беретяся по стандарту до смого кінця строки
# print(numbers[:7]) - початковий індекс не вказаний, береться від самого начала по дефолту

# Зріз з кроком

# print(numbers[::2]) - з кроком два буде брати, кожен другий символ в строці

# print(numbers[::3]) - з кроком три буде брати, кожний третій символ в строці

# print(numbers[::-1]) - відємний крок, перевертає кроки в зворотньому напрямку

# print(text[2::2])
# print(text[:5:4])
# print(text[6:10:3])

# До правил зрізаниз підстрок ми можемо зостосовувати також метод строк
names = "john asel vera"
# print(names[:4].title())
# print(names.title())



# Продовження теми методи строк

# Методи , котрі повертають методи строки

# .startswith()

text = "London is the of Great Britian"
# print(text.startswith("London")) # повертає True

# Що таке True/False?
# Це тип даних Boolean Type. Логічні змінні.
# True = правда, False - не правда

# print(text.startswith("The")) #False
# False -Так як строка не починається на слово The

# startswith - Це метод строк яка перевіряє, що срока
# починається на визначену підстроку чи символу.

# mobile = "+996 999 13 44 94"
# print(mobile.startswith("+996"))


# .endswith() - Метод строк, який перевіряє, чи строка закінчується
#  на вибіркову строку чи підстроку

# text = "I am football player."
# print(text.endswith(".")) # True. Строка дійсно закінчується на символ крапка

# date = "username_password"
# print(date.endswith("password ")) # True

# mobile = "0999134494 "
# print(mobile.endswith("099134494"))

# email = "sowdirecr@gmail.com"
# print(email.endswith("@gmail.com"))
# print(email.endswith("@mail.ru"))

# isupper() - Повертає True, якщо всі символи строки заглавні (верхнього реністру)

# text = "Abc"
# print(text.isupper())
# text2 = "ABCf"
# print(text2.isupper())
# text3 = "ABC21"
# print(text3.isupper())
#  При перевірці враховується тільки алфавітні символи і інші символи не впливають
# на перевірку

# islower() - Повертає  Trur, якщо всі символи маленькі (нижнбого регістру)
# text = "abc"
# print(text.islower()) #True

# text2 = "Abcef"
# print(text2.islower()) # False, тому що є один символ верхнього регістру

# text3 = "abc45"
# print(text3.islower()) #True, звичайні не алфавітні символи не враховуються



