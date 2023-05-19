# # Задача No1: Лотерея
# # Реализуйте свою игру лотереи с выбором числа или набора чисел
# #
#
# human_choice = int(input('Enter the number from 0 to 111:'))
# import random
#
# skynet_choice = random.randint(0, 111)
#
# if human_choice == skynet_choice:
#     print('You are win!')
# else:
#     print('You are not win!')
# print('Skynetchoice was: {}'.format(skynet_choice))
#
# # Задача No2:
# # Человек вводит день и месяц своего рождения,
# # выведите, кем он является по знаку зодиака

# date = int(input('Enter the date of your birth:'))
# month = int(input('Enter the month of your birth:'))
#
# if 1 <= date <= 21 and month == 1 or 22 <= date <= 31 and month == 12:
#     print("You are Capricorn")
# elif 1 <= date <= 21 and month == 2 or 22 <= date <= 31 and month == 1:
#     print("You are Aquarius")
# elif 1 <= date <= 21 and month == 3 or 22 <= date <= 31 and month == 2:
#     print("You are Pisces")
# elif 1 <= date <= 21 and month == 4 or 22 <= date <= 31 and month == 3:
#     print("You are Aries")
# elif 1 <= date <= 21 and month == 5 or 22 <= date <= 31 and month == 4:
#     print("You are Taurus")
# elif 1 <= date <= 21 and month == 6 or 22 <= date <= 31 and month == 5:
#     print("You are Gemini")
# elif 1 <= date <= 21 and month == 7 or 22 <= date <= 31 and month == 6:
#     print("You are Cancer")
# elif 1 <= date <= 21 and month == 8 or 22 <= date <= 31 and month == 7:
#     print("You are Leo")
# elif 1 <= date <= 21 and month == 9 or 22 <= date <= 31 and month == 8:
#     print("You are Virgo")
# elif 1 <= date <= 21 and month == 10 or 22 <= date <= 31 and month == 9:
#     print("You are Libra")
# elif 1 <= date <= 21 and month == 11 or 22 <= date <= 31 and month == 10:
#     print("You are Scorpio")
# else: print("You are Sagittarius")


# Задача No3: Творческое задание
# Придумать свою задачу на тему занятия. Обязательно
# использовать несколько вложений if-else(elif)

# Write a program that will determine the type of solution,
# the mass fraction of the solute and the solubility coefficient

mass_of_substance = float(input("Enter the mass of the substance:"))
mass_of_solvent = int(input("Enter the mass of the solvent:"))

solubility_coefficient = mass_of_substance / mass_of_solvent * 100
the_mass_fraction = mass_of_substance / (mass_of_solvent + mass_of_substance) * 100

if 0.001 <= mass_of_substance <= 1:
    print("The solution is slightly soluble ")
elif mass_of_substance > 1:
    print("The solution is soluble")
else:
    print("The solution is insoluble")

print("The mass fraction of the solute is {}%".format(the_mass_fraction))
print("The mass fraction of the solubility coefficient is {}%".format(solubility_coefficient))
