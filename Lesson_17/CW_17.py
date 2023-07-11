# class House:
#     color = 'grey'
#
#     def __init__(self, model, size):
#         self.model = model
#         self.size = size
#
#     def build(self):
#         pass
#
#     def anti_build(self):
#         self.size -= 1
#         return self.size
#
#
# village = House('модель', 9)
# print(dir(House))
# print(village.model, village.color)
# print(village.anti_build())
# town_house = House('загородное жилье', 2)
# town_house.color = 'green'
# print(town_house.color)
# print(town_house.model)
# print(town_house.anti_build())


# Создайте класс Example. В нём пропишите 3 (метода) функции. Две
# переменные задайте статически, две динамически.
# Ȃервая функция: создайте переменную и выведите её
# Вторая функция: верните сумму 2-ух глобальных переменных
# Третья функция: верните результат возведения первой динамической
# переменной во вторую динамическую переменную
# Создайте объект класса.
# Ȁапечатайте обе функции
# Ȁапечатайте переменную a

# class Example:
#     static_var1 = 1
#     static_var2 = 2
#
#     def first_function(self):
#         per = 3
#         print(per)
#
#     def second_function(self):
#         return Example.static_var1 + Example.static_var2

class Calculator:
    def input_numbers(self):
        num1 = float(input("Enter 1 number: "))
        num2 = float(input("Enter 2 number: "))
        return num1, num2

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Division by zero!")
            return None


calculator = Calculator()
numbers = calculator.input_numbers()
result_add = calculator.add(numbers[0], numbers[1])
result_subtract = calculator.subtract(numbers[0], numbers[1])
result_multiply = calculator.multiply(numbers[0], numbers[1])
result_divide = calculator.divide(numbers[0], numbers[1])

print("Результат сложения:", result_add)
print("Результат вычитания:", result_subtract)
print("Результат умножения:", result_multiply)
print("Результат деления:", result_divide)