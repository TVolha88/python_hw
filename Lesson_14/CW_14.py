# f = open('example.txt', 'r')
# print(f)
# print(*f)
# f.close()

# with open('new_file.txt', 'w') as f:
#     print(f)
#     f.write('Hello my friend!')

# import os
# # os.rename('new_file.txt', 'my_new_file.txt')
#
# print(f"Current catalog is {os.getcwd()}")
# print(f"Make directory {os.getcwd('new_dir_Lesson_14')}")
# print(f"Change directory {os.chdir('..')}")

# print(f"Current catalog is {os.getcwd()}")
# print(f"Make directory {os.mkdir('new_dir_les_13_1')}")

with open('task_1.txt', 'r') as f:
    s = f.readlines()
    print(s)
for i in s:
    i = i.replace('_', ' ')
    a = i.split(' ')
    print(a)
summa = 0
for i in a:
    if i.isdigit():
        i = int(i)
        summa = summa + i
print(summa)




