
# Два метода в классе, один принимает в себя либо
# строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв
# меньше или равно длине слова, выводить все
# гласные, иначе согласные;
# если число то, произведение суммы чётных цифр
# на длину числа.
# Длину строки и числа искать во втором методе

class Homework:
    def process_input(self, input_data):
        if isinstance(input_data, str):
            return self.process_string(input_data)
        elif isinstance(input_data, int):
            return self.process_number(input_data)
        else:
            print("Ошибка: неподдерживаемый тип данных!")
            return None

    def process_string(self, input_string):
        vowels = ['a', 'e', 'i', 'o', 'u']
        consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        vowel_product = 1
        consonant_product = 1

        for char in input_string:
            if char.lower() in vowels:
                vowel_product *= len(input_string)
            elif char.lower() in consonants:
                consonant_product *= len(input_string)

        if vowel_product <= len(input_string):
            return [char for char in input_string if char.lower() in vowels]
        else:
            return [char for char in input_string if char.lower() in consonants]

    def process_number(self, input_number):
        even_sum = 0
        length = len(str(input_number))

        for digit in str(input_number):
            if int(digit) % 2 == 0:
                even_sum += int(digit)

        return even_sum * length


homework = Homework()

# Примеры использования
input_data1 = "hello"
result1 = homework.process_input(input_data1)
print("Результат для строки 'hello':", result1)

input_data2 = "python"
result2 = homework.process_input(input_data2)
print("Результат для строки 'python':", result2)

input_data3 = 12345
result3 = homework.process_input(input_data3)
print("Результат для числа 12345:", result3)

input_data4 = 2468
result4 = homework.process_input(input_data4)
print("Результат для числа 2468:", result4)
