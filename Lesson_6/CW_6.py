# for i in range(10):
#     print(i)
# for i in 'i"m learning python':
#     print(i)

# for i in range(15, 1, -1):
#     print(i)

# str = input("Enter the str:")
# symbol = input("Symbol")
# new_str = ""
# for i in str:
#     if i == symbol:
#         continue
#
#     new_str += i
# print(new_str)

# for i in range(100, 900, 5):
#     if i % 100 == 0:
#         print(i)
#

# for i in range(94, 351):
#     if i % 5 == 0:
#         print(i)

# Дан массив из 7 цифр. Если четных цифр в нем больше чем
# нечетных, то найти сумму всех цифр массива, если нечетных
# больше, то найти произведение 1, 3, 6 элементов
# lst = [1, 2, 3, 4, 5, 6, 7]
# even, odd = 0, 0
# for i in lst:
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i
#
# if even > odd:
#     print("Четных больше", sum(lst))
#
# if even < odd:
#     print("Нечетных больше", ",", "Произведение:", lst[0] * lst[2] * lst[5])

# lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum = 0
# pr = 1
#
# for i in lst1:
#     sum += i
#     pr *= i
#
# print(sum, pr)

# for i in range(10, 510, 100):
#     for j in range(10, 51, 10):
#         print(i + j)
#     print("OK")
# print("OK1")

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end=' ')
    print("")
