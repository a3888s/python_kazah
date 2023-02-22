# from random import randint, choice
#
#
# class Player:
#
#     def __init__(self, name):
#         self.name = name
#         self.__health = 250
#         # self.__armor = 100
#         self.protection = False
#         self._max_damage = 50
#         self._min_damage = 10
#
#     def attack(self, target):
#         dodge_list = [True, True, True, True, False]
#         # target - ціль атаки, який також являється об'єктом класу Player.
#         if isinstance(target, Player):
#             if target.protection:
#                 print("Удар по щиту")
#             else:
#                 if choice(dodge_list):
#                     current_damage = randint(self._min_damage, self._max_damage)
#                     target.health_minus(current_damage)
#                     print(f"{target.name} отримав {current_damage} урону")
#                     target.get_player_info()
#                     target.check_health_status()
#                 else:
#                     print(f"{self.name} промазав!!!")
#         else:
#             print("Ви не можете атакувати дану ціль")
#
#     def health_minus(self, damage_amount):
#         self.__health -= damage_amount
#
#     def check_health_status(self):
#         if self.__health <= 0:
#             print(f"{self.name} програв гру")
#             exit(1)
#
#     def get_player_info(self):
#         print(f"Стан здоров'я: {self.__health} HP")
#
#     def active_protection(self):
#         if self.protection:
#             self.protection = False
#         else:
#             self.protection = True
#
#
# print("Гра починається!...")
# name1 = input("Гравець 1 введіть імя: ")
# name2 = input("Гравець 2 введіть імя: ")
# player1 = Player(name1)
# player2 = Player(name2)
#
# active = True
while active:
    player1_action = input(f"{player1.name} виберіть дію(a/p): ")
    if player1_action.strip().lower() == "a":
        player1.attack(player2)
    else:
        player1.active_protection()

    player2_action = input(f"{player2.name} виберіть дію(a/p): ")
    if player2_action.strip().lower() == "a":
        player2.attack(player1)
    else:
        player2.active_protection()






