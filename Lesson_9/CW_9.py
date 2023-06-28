# import random
#
# c = [random.randint(0, 100) for i in range(10)]
# print(c)
# c = [i for i in range(10)]
# print(c)

# l1 = [1, 2, 3]
# l2 = l1[2:]
# print(l2, type(l2))


# lst = [1, 2, 3, 7, 9, 11]
# print(lst[::-1])

# lst = [1, 2, 3, 7, 9, 11, 20]
#
# ind = lst.index(20)
# lst[ind] = 200
# print(lst)

#
# lst = [1, 2, 3, 7, 9, 11]
# sum_1 = 0
# sum_2 = 0
#
# for i in lst:
#     if i % 2 == 0:
#         sum_1 = sum_1 + 1
#     else:
#         sum_2 = sum_2 + 1
# print("chetnyh: {}, nechetnyh: {}".format(sum_1, sum_2))
#
# if sum_1 < sum_2:

# a = [5, [1,2], 2, 'r', 4, 'ee']
# b = [4, 'we', 'ee', 3, [1,2]]
# c = []
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)

a = [4, 6, 'py', 'tell', 78]
b = [44, 'hello', 56, 'exept', 3]


a.extend(b)
a.insert(3, 6)
print(a)
for i in a:
    if type(i) == str:
        a.remove(i)
print(a)
print(len(a))
