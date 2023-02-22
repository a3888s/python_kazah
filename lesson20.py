# Робота з файлами.

# Контектний менеджер в python - with ... as ...

# with open("test.txt", encoding="utf-8") as file:
#     text= file.read()
#     print(text)

# Як тільки ми пишемо код поза контексту файлу
# Ми втрачаємо доступ до файлу і не можемо проводити дії.
# text2 = file.read()
# print(text2)

# Запис в контексті

# with open("new_file.txt", "w", encoding="utf-8") as file:
#     file.write("Text from in context")

# Завданя - 2
# Прочитайте файл students.txt.
# Там зберігаються імена студентів і їх оцінки.
# Ваша программа повинна знаходити середню оцінку в даному файлі.
# Доп. завдання: Запишіть середню оцінку назад у файл.
# Доп. задача: Знайдіть студента з самим лучшим баллом і добавте його в файл
# Кращий бал: Askar-97

# with open("students.txt", "r+", encoding="utf-8") as file:
#     lines = file.readlines()
#     marks = []
#     best_student = [0, "best_student"]
#     for l in lines:
#         l = l.strip().split("-")
#         mark = float(l[1])
#         marks.append(mark)
#         s_mark = sum(marks)/len(marks)
#         s_mark = round(s_mark,2)
#         if best_student[0] < mark:
#             best_student[0] = mark
#             best_student[1] = l[0]
#     file.write(f"Середня оцінка-{s_mark} \nНайкраща оцінка - {best_student}")
#     file.close