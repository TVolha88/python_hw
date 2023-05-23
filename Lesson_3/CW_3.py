# # print(5 == 5)
# # print(5 == 4)
# #
# # print(5 != 5)
# # print(5 != 4)
# #
# # print(5 > 5)
# # print(5 > 4)
# #
# # print(5 >= 5)
# # print(5 >= 4)
#
# # a=5
# # if a>=5:
# #     print('perfect')
# # else:
# #     print('think about it more')
#
# num = int(input("Enter the number:"))
#
# if num % 2 == 0:
#     print("четное число")
# else:
#     print("нечетное число")
#
# Задание No9
#
# Напишите программу, которая считывает строку и
# проверяет является ли она словом 'Mister'
#
# string = input()
# is_mister = (string == "Mister")
# print(is_mister)

# Задание No10
#
# Напишите программу, которая принимает на вход:
# 1. Цвет доспехов(строка). Возможные варианты: red, yellow,
# black
# 2. Цвет щита(строка). Возможные варианты: red, yellow, black
# Программа выводит True если цвет доспехов не красный и
# цвет щита чёрный. В остальных случаях выводит False

# armor_color = input("Enter the armor color: ")
# shield_color = input("Enter the shield color: ")
#
# if armor_color != 'red' and shield_color == 'black':
#     print(True)
# else:
#     print(False)

armor_color = input("Enter the armor color: ")
shield_color = input("Enter the shield color: ")

is_knight = (armor_color!= 'red' and shield_color == 'black')
print(is_knight)
