### Урок 5: Списки в Python

# 1. Введение в списки
# - Что такое список?
# - Отличие списка от других типов данных
# - Синтаксис создания списков

# 2. Индексация и доступ к элементам
# - Доступ по индексу
# - Отрицательные индексы
# - Изменение элементов списка

# 3. Основные операции со списками
# - Длина списка (len())
# - Конкатенация списков (+)
# - Дублирование элементов (*)
# - Проверка вхождения (in)

# 4. Методы списков
# - append(), insert() – добавление элементов
# - remove(), pop() – удаление элементов
# - index(), count() – поиск элементов
# - sort(), reverse() – сортировка и разворот

# 5. Срезы списков
# - Получение подсписков

# 7. Вложенные списки
# - Создание двумерных списков
# - Доступ к элементам вложенного списка


# Список (list) – это упорядоченная изменяемая коллекция элементов.

# Пример списка
fruits = ["яблоко", "банан", "апельсин"]
animals = []
# print(fruits[0])  # яблоко
# print(fruits[-1])  # апельсин

# fruits[1] = "груша"
# print(fruits)
# Списки могут содержать разные типы данных
mixed_list = [42, "hello", 3.14, [1, 2, [33, 55, 77]]]
# print(mixed_list[3][2][0])  # Доступ ко второму элементу вложенного списка → 2

# negative indexes
# print(mixed_list[-1][-1][-1])

# editing index
# print(mixed_list)
# print(mixed_list[1])
mixed_list[1] = "first lesson"
mixed_list[2] = 33.11
# print(mixed_list)
only_digits = [1, 2, 3, 4]
# print(len(only_digits), sum(only_digits))

concatenated_list = mixed_list + fruits + only_digits
# print(concatenated_list)

# print(fruits * 2)
ones = [1] * 10
# print(ones)

# print(fruits)
# print("апельсин" in fruits)
# print("Банан" in fruits)
# print("bananas" in mixed_list)

# 4. Методы списков
# - append(), insert() – добавление элементов
# - remove(), pop() – удаление элементов
# - index(), count() – поиск элементов
# - sort(), reverse() – сортировка и разворот
# print(fruits)
fruits.append("ананас")
# print(fruits)
fruits.insert(2, "груша")
# print(fruits)
returned_value = fruits.pop()
# print(returned_value)
# print(fruits)
# print(mixed_list)
# mixed_list.pop()

# print(mixed_list)
mixed_list.remove('first lesson')
# print(mixed_list)

# mixed_list.append(33.11)
# print(mixed_list)
# print(mixed_list.index(33.11))
# # print(mixed_list)
# print(mixed_list.count(33.11))
# mixed_list.append(33.11)
# print(mixed_list)
# print(mixed_list.count(33.11))
# print(mixed_list)

numbers = [2, 6, 1, 9, 3, 4, 7]
# print(numbers)
# num2 = sorted(numbers)
# print(num2)
# print(numbers)
# numbers.sort()
# print(numbers)
#
print(numbers)
# print(numbers[2:4])  # [start(including):stop(not including):step]
# print(numbers[-2:1:-4])
print(numbers[::-1])


# ---- Задачи для закрепления ----

# 1. Создание и работа со списками
# Создай список с 5 любимыми блюдами и выведи третий элемент.

# 2. Индексация
# Дан список чисел [10, 20, 30, 40, 50].
# Используя индексы, замени 30 на 99 и выведи список.

# 3. Операции со списками
# Создай два списка: ["a", "b", "c"] и [1, 2, 3].
# Объедини их в один и выведи результат.

# 4. Методы списка
# Дан список [4, 2, 9, 1].
# - Добавь 7 в конец.
# - Удали 2.
# - Отсортируй список.
# - Выведи результат.

# a = [1, 2, 3, 4]

# 5. Работа со срезами
# Дан список ["python", "java", "c++", "javascript", "php"].
# - Выведи первые три элемента.
# - Выведи список в обратном порядке.

# 6. Итерация по списку
# Дан список имен ["Аня", "Борис", "Вика"].
# выведи приветствие для каждого:
# > Привет, Аня!
# > Привет, Борис!
# > Привет, Вика!

# 7. Вложенные списки
# Дан список [[1, 2], [3, 4], [5, 6]].
# Выведи 4, обратившись к элементу по индексу.
