# 1. Ȃеремножить все нечётные значения в диапазоне от 1 до 30.

pr = 1
for i in range(1, 31):
    if i % 2 != 0:
        pr *= i
print(pr)
print('=' * 35)

# 2. Записать в массив все числа в диапазоне от 1 до 100 кратные 5.

arr = []
for i in range(1, 101):
    if i % 5 == 0:
        arr.append(i)
print(arr)
print('=' * 35)

# 3. Вывести на экран все чётные значения в диапазоне от 1 до 71.

for i in range(1, 72):
    if i % 2 == 0:
        print(i, end=' ')
print(sep='\n')
print('=' * 35)

# 4. Дан массив чисел. Если число встречается более двух раз, то добавить
# его в новый массив.

arr = [1, 6, 8, 345, 679, 1, 4, 5, 3, 6, 7, 9, 3, 9, 3, 4, 6, 6, 7, 8, 10]
new_arr = []
for i in arr:
    if arr.count(i) >= 2:
        new_arr.append(i)
print(new_arr)