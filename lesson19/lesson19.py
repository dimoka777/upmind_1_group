# === Урок 19: Модули и пакеты ===

# 🔹 Что такое модуль?
# Модуль — это файл с кодом на Python, который можно импортировать в другие файлы.
# Каждый файл .py — это модуль.

# Пример создания модуля:
# В файле math_utils.py:
# def add(a, b):
#     return a + b

# В другом файле:
# import math_utils
# print(math_utils.add(2, 3))  # Вывод: 5

# 🔹 Способы импорта модулей:

# 1. import module
# import math
# print(math.sqrt(16))

# 2. from module import function
# from math import sqrt
# print(sqrt(25))

# 3. from module import *  (не рекомендуется)
# from math import *
# print(sqrt(36))

# 4. import module as alias
# import math as m
# print(m.sqrt(49))

# 🔹 Встроенные (стандартные) модули:
# import random, datetime, os, sys, json

# 🔹 Установка сторонних модулей:
# pip install requests

# 🔹 Что такое пакет?
# Пакет — это папка с файлами Python и файлом __init__.py
# Пример:
# my_package/
# ├── __init__.py
# ├── module1.py
# └── module2.py

# Пример использования:
# from my_package import module1

# 🔹 Проверка пути к модулям:
# import sys
# print(sys.path)

# 🔹 Создание собственного пакета:
# - Создай папку
# - Добавь туда модули
# - Вставь __init__.py
# - Используй from имя_пакета import модуль

# --- Ознакомительные задачи (10) ---

# 1. Импортируй модуль math и выведи квадратный корень из 64.
# 2. Импортируй только функцию sqrt из модуля math и вычисли sqrt(81).
# 3. Используй псевдоним для math и вычисли косинус 0.
# 4. Выведи текущую дату с помощью модуля datetime.
# 5. Импортируй модуль random и выбери случайное число от 1 до 100.
# 6. Используй модуль os, чтобы получить текущую директорию.
# 7. Прочитай sys.argv из модуля sys.
# 8. Импортируй json и преобразуй словарь в строку.
# 9. Установи модуль requests и проверь его импорт.
# 10. Создай свой модуль с функцией say_hello() и используй его.


