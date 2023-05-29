# Казино. Компьютер генерирует числа от 1 до 10 и от 1 до 2-х
# соответственно. Цифры от одного до 10 отвечают за номера, а от 1
# до 2 за цвета (1 красный, 2 черный).
# Ȃользователю дается 5 попыток угадать номер и цвет (Ȃрим.
# введения с клавиатуры: 3 красный). В случае неудачи вывести на
# экран правильную комбинацию.

import random

attempt = 0

skynet_number = random.randint(1, 10)
skynet_color = random.randint(1, 2)

while attempt <= 5:

    num = int(input("Enter the number from 1 to 10:"))
    color = int(input("Enter the color from 1 to 2(where 1 - is red and 2 - is black):"))
    attempt += 1

    if num == skynet_number and color == skynet_color:
        print("You win!")
        break
    else:
        num != skynet_number and color != skynet_color
        print("You lose! The number is {} and the color is {}.".format(skynet_number, format(skynet_color)))




