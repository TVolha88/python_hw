# Задача №1
# Дана строка.
# Ȅначала выведите третий символ этой строки.
# Во второй строке выведите предпоследний символ этой строки.
# В третьей строке выведите первые пять символов этой строки.
# В четвертой строке выведите всю строку, кроме последних двух символов.
# В пятой строке выведите все символы с четными индексами (считая, что индексация начинается
# с 0, поэтому символы выводятся начиная с первого).
# В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго
# символа строки.
# В седьмой строке выведите все символы в обратном порядке.
# В восьмой строке выведите все символы строки через один в обратном порядке, начиная с
# последнего.
# В девятой строке выведите длину данной строки.

string = "Hello, world!"

print(string[2])
print(string[-2])
print(string[:5])
print(string[:11])
print(string[::2])
print(string[1::2])
print(string[::-1])
print(string[::-2])
print(len(string))

# Напишите программу, которая запрашивает у
# пользователя его имя, а затем выводит строку$ git pull origin master
# «Привет, …», где вместо многоточия имя
# пользователя. А вторая строка выведет имя
# пользователя с повтором 3 раза.

print('-' * 21)

name = input("Input your name")
print('Hello, {}!'.format(name))
print(f'Hello, {name}!')
print(name * 3)

# Вычислить сумму цифр случайного трёхзначного
# числа

print('-' * 21)

import random

number = random.randint(100, 999)

number = str(random.randint(100, 999))
a1 = number[0]  # 1
a2 = number[1]  # 2
a3 = number[2]  # 3
print(a1, type(a1), a2, type(a2), a3, type(a3))
s = int(a1) + int(a2) + int(a3)
print(s)

# Ȁа вход подается непустая строка S. В строке хотя бы два символа.
# 1) В первой строке распечатайте каждый 3-й символ, начиная с
# нулевого (подряд, не разделяя символы пробелами).
# 2) Во второй строке распечатайте первый и последний символы
# (подряд, не разделяя символы пробелами).
# 3) В третей строке распечатайте S в верхнем регистре.
# 4) В четвертой строке распечатайте S в обратном порядке.
# 5) В пятой строке напечатайте True, если все символы в строке S —
# цифры и False в противном случае.

print('-' * 21)

s = "Hello,world"
print(s[::3])
print(s[0] + s[-1])
print(s.upper())
print(s[::-1])
print(s.isdigit())

# Вводиться строка. Ȇдалить из неё все пробелы. Ȃосле этого
# определить, является ли она палиндромом (перевертышем),
# т.е. одинаково пишется, как сначала, так и с конца

print('-' * 21)

s = 'Hello, world!'
s = s.split()
print(s)
s = ''.join(s)
print(s)
# hello, world == dlrow ,olleh
if s == s[::-1]:
    print('Im polindrom')
else:
    print('No')

# Дана строка, состоящая ровно из двух слов, разделенных
# пробелом.
# Ȃереставьте эти слова местами. ȃезультат запишите в
# строку и
# выведите получившуюся строку.
# Замените в этой строке все цифры 1 на слово one
# Ȃримечание: решить без использования функции split

print('-' * 23)

s_5 = 'hel1lo worl1d'
print(s_5.find(' '))
f_w = s_5[:s_5.find(' ')]  # s_5[:6]
f = s_5[s_5.find(' ') + 1:] + ' ' + f_w  # s_5[7:]
print(f)
print(f.replace('1', 'one'))
