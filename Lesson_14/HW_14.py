# Создать текстовый файл, записать в него построчно данные, которые
# вводит пользователь. ȁкончанием ввода пусть служит пустая строка.


with open('file.txt', 'w') as f:
    while True:
        line = input('Enter the string (empty string to end): ')

        if not line:
            break

        f.write(line + '\n')

# В текстовом файле посчитать количество строк, а также для каждой
# отдельной строки определить количество в ней символов.

with open('file1.txt', 'r') as f:
    num_lines = 0
    for line in f:
        num_lines += 1
        num_chars = len(line.strip())
        print(f'String {num_lines}: {num_chars} elemets')

    print(f'Total lines: {num_lines}')

# Есть массив состоящий из слов и чисел, нужно записать в
# файл сначала слова в порядке их длины, а после слов
# цифры в порядке возрастания


arr = [11, 17, 'hello', 'world', 2, 'python', 101]
word_list = []
number_list = []

for elem in arr:
    if isinstance(elem, str):
        word_list.append(elem)
    else:
        number_list.append(elem)

word_list.sort(key=len)

number_list.sort()

with open('file3.txt', 'w') as f:
    for elem in word_list:
        f.write(elem + '\n')
    for elem in number_list:
        f.write(str(elem) + '\n')
