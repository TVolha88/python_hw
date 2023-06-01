# ЗАДАНИЕ 1. По двум введенным пользователем катетам вычислить длину
# гипотенузы.

import math

kat_1 = int(input("Enter the length of the first cat.:"))
kat_2 = int(input("Enter the length of the second cat.:"))

print(math.hypot(kat_1, kat_2))
print(math.sqrt(kat_1 ** 2 + kat_2 ** 2))

# ЗАДАНИЕ 2. Вводятся три разных числа. Найти, какое из них является
# средним(больше одного, но меньше другого).

num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))
num_3 = int(input("Enter the third number:"))

if num_1 > num_2 and num_1 < num_3:
    print(f"The middle number is {num_1}")
elif num_2 > num_1 and num_2 < num_3:
    print(f"The middle number is {num_2}")
else:
    print(f"The middle number is {num_3}")

# ЗАДАНИЕ 3. Из двух случайных чисел, одно из которых четное, а другое
# нечетное, определить и вывести на экран нечетное число.

num_1 = int(input("Enter the even number:"))
num_2 = int(input("Enter the odd number:"))

if num_1 % 2 == 0:
    print(f"The odd number is {num_2}")

elif num_2 % 2 == 0:
    print(f"The odd number is {num_1}")

# ЗАДАНИЕ 4. Сформировать из введенного числа обратное по порядку
# входящих в него цифр и вывести на экран. Например, если
# введено число 3486, то надо вывести число 6843.

num = int(input("Number:"))
s = str(num)
print(s[::-1])

# ЗАДАНИЕ 5.  Найти площади прямоугольника, треугольника или круга.
# примечание: надо ввести фигуру 1-прямоугольник, 2-треугольник,
# 3-круг.

figure = int(input("Please, choose the figure ( 1 - rectangle, 2 - triangle, 3 - circle): "))

if figure == 1:
    side_1 = int(input("Enter the length of the side 1:"))
    side_2 = int(input("Enter the length of the side 2:"))
    print('The S of the rectangle is:', side_1 * side_2)

if figure == 2:
    side_1 = int(input("Enter the length of the side 1:"))
    side_2 = int(input("Enter the length of the side 2:"))
    print('The S of the triangle is:', (side_1 * side_2) / 2)

if figure == 3:
    side_3 = int(input("Enter the radius of the circle:"))
    print('The S of the circle is:', 3.14 * (side_3 ** 2))


# ЗАДАНИЕ №6. Определить существование треугольника по трем сторонам
# Примечание: У треугольника сумма любых двух сторон должна
# быть больше третьей. Иначе две стороны просто "лягут" на третью
# и треугольника не получится.

side_1 = int(input("Side 1:"))
side_2 = int(input("Side 2:"))
side_3 = int(input("Side 3:"))


if side_1 + side_2 > side_3 or side_1 + side_3 > side_2 or side_2 + side_3 > side_1:
    print("This is triangle")

else:
    print("This is not triangle")


# ЗАДАНИЕ №7. Принадлежит ли точка кругу
# Примечание: Если выбрать точку на координатной плоскости,
# то можно увидеть, что проекции ее координат на оси x и y
# являются катетами прямоугольного треугольника. А гипотенуза
# этого прямоугольного треугольника как раз показывает
# расстояние от начала координат до точки. Таким образом, если
# длина гипотенузы будет меньше радиуса круга, то точка будет
# принадлежать кругу; иначе она будет находится за его
# пределами.


import math


x = float(input("Введите координату x точки: "))
y = float(input("Введите координату y точки: "))
r = float(input("Введите радиус круга: "))


distance = math.sqrt(x**2 + y**2)


if distance <= r:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")

# ЗАДАНИЕ №8
# Вводится строка, состоящая из слов, разделенных пробелами.
# Требуется посчитать количество слов в ней.

str = input("Enter the string:")
words = str.split()
print(len(words))


# ЗАДАНИЕ №9
# Введите строку c клавиатуры, которая состоит из букв разных
# регистров. Нужно очистить эту строку от всех заглавных букв и
# вывести результат на экран.

str = input("Enter the string:")
str = str.lower()
print(str)


# ЗАДАНИЕ №10
# Написать программу, которая выводит числа от 0 до 100 на экран,
# пропуская числа кратные 7

for i in range(1, 101):
    if i % 7 == 0:
        print(i)


# ЗАДАНИЕ №11
# Найти сумму ряда чисел от 1 до 100. Полученный результат
# вывести на экран

sum = 0
for i in range(1, 101):
    sum += i
    print(sum)

# ЗАДАНИЕ №12
# Факториалом числа n называется произведение 1 × 2 × ... × n.
# Обозначение: n!.
# По данному натуральному n вычислите значение n!. Пользоваться
# математической библиотекой math в этой задаче запрещено.

n = int(input("Enter the number:"))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(factorial)

# ЗАДАНИЕ №13
# Пользователь передает целое положительное число N,
# выведете на экран последовательность от 1 до N "ёлочкой",
# например для N=17:

n = int(input('Enter the number:'))

q = 1
s = 1
k = 0
while q <= n:
    print(q, end=' ')
    q = q + 1
    k = k + 1
    if k == s:
        print()
        s = s + 1
        k = 0

# ЗАДАНИЕ №14
# Найти пересечения в 2 списках и записать в 3 список эти
# пересечения

list_1 = [1, 2, 3]
list_2 = [3, 4, 5, 6]
list_3 = []

for i in list_1:
    if i in list_2:
        list_3.append(i)
print(list_3)

