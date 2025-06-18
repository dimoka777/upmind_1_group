# 🔢 Integer (int) Methods
# print("🔢 Integer Methods")

# int() -
num = -10
# print("Absolute value:", abs(num))  # убирает отрицательный знак у числа
# print("Max of (10, 20, 30):", max(10, 20, 30))  # находит максимальное число из списка
# print("Min of (10, 20, 30):", min(10, 20, 30))  # находит минимальное число из списка
# print("Power (2^3) using pow():", pow(2, 3))  # возведение в степень
# print("Power (2^3) using **:", 2 ** 3)  # возведение в степень
# print("Convert '100' to int:", int("100"))  # конвертация строки 100 в число
# print("Convert float 3.9 to int:", int(3.9))  # конвертация флоата в число с округлением в меньшую сторону

# # 🟡 Float (float) Methods
# print("\n🟡 Float Methods")  # число с плавающей точкой
#
fnum = -7.8
# print("Absolute value:", abs(fnum))  # переводит число с отрицательного в положительное
# print("Round 4.678:", round(4.678))  # округление
# print("Round 4.678 to 2 decimals:", round(4.6786, 3))  # округление до двух знаков после запятой
# print("Convert '10.5' to float:", float("10.5"))  # конвертация строки во флоат(число с плавающей точкой)
#
# # 🔠 String (str) Methods
# print("\n🔠 String Methods")  # строка
#
# test_string = "  Hello World  "
# print("Uppercase:", test_string.upper())  # изменяет маленькие буквы на большие
# print("Lowercase:", test_string.lower())  # изменяет большие буквы на маленькие
# print("Title Case:", "hello world".title())  # изменяет первые буквы в каждом слове на большие
# print("Capitalized:", "hello World".capitalize())  # изменяет первые буквы в каждом слове на большие
# print("Stripped spaces:", test_string.strip())  # удаляет пробелы с начала и конца строки
# print("Left stripped:", test_string.lstrip())  # удаляет пробелы с начало строки
# print("Right stripped:", test_string.rstrip())  # удаляет пробелы с конца строки
# print("Index of 'World':", test_string.find("World"))  # поиск строки или символа в строке
# print("Replace 'Hello' with 'Hi':", test_string.replace("Hello", "Hi"))  # замена подстроки в строке
# fruits = "apple,banana,orange"
# words = fruits.split(",")  # делим строку на подстроки через делитель
# print("Split string:", words)
# print("Joined string:", "-".join(words))  # соединяем строки в одну строку через делитель
# print("Starts with 'Hello':", test_string.startswith("Hello"))  # проверяет начинается ли строка с подстроки
# print("Ends with 'World':", test_string.endswith("World"))  # проверяет заканчивается ли строка подстрокой
# print("Is '12345' all digits?:", "12345".isdigit())  # проверяет является ли строка числом
# print("Is 'abc' all letters?:", "abc".isalpha())  # проверяет состоит ли строка из символов алфавита
# print("Is 'abc123' alphanumeric?:", "abc123".isalnum())  # проверяет состоит ли строка из букв или цифр
# print("Is '   ' all spaces?:", "   ".isspace())  # проверяет состоит ли строка из пробелов, табов
#
# # 🔵 Boolean (bool) Methods
# print("\n🔵 Boolean Methods")  #

# print("Boolean of 0:", bool(0))  # False
# print("Boolean of 1:", bool(1))  # True
# print("Boolean of empty string:", bool(""))  # False
# print("Boolean of non-empty string:", bool("hello"))  # True
# print("Boolean of None:", bool(None))  # False
# print("Boolean of empty list:", bool([]))  # False
# print("Boolean of non-empty list:", bool([1, 2, 3]))  # True

# # 🎯 Formatting Strings using f-strings
# name = input("What is your name: ")
# age = input("What is your age: ")
# print(f"My name is {name} and I am {age} years old.")


a = '2'
b = '3'
print(a + b)