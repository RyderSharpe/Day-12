# ################### Scope ####################
#
# enemies = 1
#
# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")
#
# # local scope
# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)
#
# drink_potion()
#
# # Global scope
# player_health = 10
#
#   def drink_potion():
#     potion_strength = 2
#     print(player_health)
#
#   drink_potion()

# ################### No Block Scope ####################

# enemies = ["skeleton", "zombie", "alien"]
# if game_level < 5:
#     new_enemy = enemies[0]
#
# print(new_enemy)

# game_level = 3
# def create_enemy():
#     enemies = ["skeleton", "zombie", "alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#
#     print(new_enemy)

# ################### Global Scope ####################
# enemies = "skeleton"
# def increase_enemies():
#   enemies = "Zombie"
#   print(f"enemies inside function: {enemies}")
#
# increase_enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# ################### Global Constants ####################
# PI = 3.24159
# URL = "https://www.google.com"
# TWITTER_HANDLE = "@handle"
#
# def calc():
#     print(PI)
#     print(URL)
#     print(TWITTER_HANDLE)

#####################################

# i = 50
#
# def foo():
#   i = 100
#   return i
#
# foo()
# print(i)


def bar():
  my_variable = 9

  if 16 > 9:
    my_variable = 16

  print(my_variable)


bar()