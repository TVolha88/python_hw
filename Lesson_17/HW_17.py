
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
            print("Error: Check the type of the data!")
            return None

    def process_string(self, input_string):
        vowels = ['a', 'e', 'i', 'o', 'u']
        consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
                      'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

        vowel_pr = 1
        consonant_pr = 1

        for char in input_string:
            if char.lower() in vowels:
                vowel_pr *= len(input_string)
            elif char.lower() in consonants:
                consonant_pr *= len(input_string)

        if vowel_pr <= len(input_string):
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

