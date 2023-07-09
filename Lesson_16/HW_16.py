# Домашнее задание
# Задача №1
# Ввод с клавиатуры. Если строка введённая с клавиатуры –
# это числа, то поделить первое на второе. ȁбработать
# ошибку деления на ноль. Если второе число 0, то
# программа запрашивает ввод чисел заново. ȅакже если
# были введены буквы, то обработать исключение.

while True:
    try:
        num1 = float(input("Enter the 1 number: "))
        num2 = float(input("Enter the 2 number: "))

        if num2 == 0:
            print("Error: Division by zero!")
            continue

        result = num1 / num2
        print("Division result:", result)
        break

    except ValueError:
        print("Error: incorrect data entered!")