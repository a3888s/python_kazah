# ООП - обєктно орієнтоване програмування

# Основи ооп:
# 1) Класс
# 2) Обєкт
# 3) Методи

# class Car():

#     # функції в середині класу називаються методатими
#     def __init__(self, model, year, color, race):
#         # Атриьбути обєкту - данні обєкти
#         self.model = model
#         self.year = year
#         self.color = color
#         self.race = race

#     def drive(self):
#         self.race += 100
#         print("Ми рухаємося вперед")
#         print(f"Ваш пробіг {self.race}")

#     def stop(self):
#         print("Машина зупинилась")
    

# car_toyota = Car('Camry', '2015', 'white', 10000)
# car_toyota.drive()
# car_toyota.drive()
# car_toyota.stop()
# while True:
#     car_toyota.drive()
#     if car_toyota.race > 15000:
#         break
# print(car_toyota.color)
# car_tayota - екземпляр классу чи обєктом классу

# class Hero():
#     def __init__(self, name, damage, protect):
#         self.name = name
#         # Атрибут за замовчуванні
#         self.health = 100
#         self.damage = damage
#         self.protect = protect

#     def attack(self, enemy):
#         print(f"{self.name} атакує")
#         enemy.health -= self.damage
#         enemy.get_health_status()
    
#     def defence(self):
#         print("Щит піднятий")

#     def get_health_status(self):
#         print(f"Життя героя: {self.name}:{self.health}")
    
# hero1 = Hero(name="Піпец", damage=5, protect=50)
# hero2 = Hero(name="Erjan", damage=5, protect=70)

# hero1.attack(hero2)
# hero2.attack(hero1)

# class House():
#
#     def __init__(self, square, floor_count, room_count, price, address):
#         self.square = square
#         self.floor_count = floor_count
#         self.room_count = room_count
#         self.price = price
#         self.address = address
#         self.sold_status = False
#         self.owner = "Без власника"
#
#     def get_hause_info(self):
#         print(f"Площа: {self.square}")
#         print(f"Кількість поверхів: {self.floor_count}")
#         print(f"Кількість кімнат: {self.room_count}")
#         print(f"Ціна будинку: {self.price}")
#         print(f"Адреса: {self.address}")
#
#     def buy(self):
#         if self.sold_status:
#             print("Будинок проданий!")
#         else:
#             name = input("Введіть ваші ФІО: ")
#             self.sold_status = True
#             self.owner = name
#             print(f"{name}, вітаємо, Ви купили дім!")
#
# house1 = House(
#     square=200,
#     floor_count=4,
#     room_count=8,
#     price=1_000_000,
#     address="м. Київ, Євгена Гуцала 3"
# )
# house1.get_hause_info()
# house1.buy()
# house1.buy()

