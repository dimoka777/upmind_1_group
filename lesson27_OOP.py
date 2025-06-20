# ООП в Python
#
# Объектно-ориентированное программирование (ООП) – это стиль
# программирования, в котором код организуется в объекты.
# Каждый объект представляет реальный предмет и обладает атрибутами
# (данные) и методами (поведение).
# Python поддерживает ООП через классы и объекты.
#
# 1. Основные принципы ООП
# 1. Классы и объекты
#
# 2. Классы и объекты
# Класс – это шаблон (чертеж) для создания объектов.
# Объект – это экземпляр класса с собственными данными.
# Пример: Класс "Автомобиль"


class Car:

    def __init__(self, brand, model, year):
        self.brand = brand # Атрибут
        self.model = model
        self.year = year

    def start_engine(self): # Метод
        return f"{self.brand} {self.model} завел двигатель!"

# Создаем объекты
car1 = Car("Toyota", "Camry", 2023)
car2 = Car("Honda", "Civic", 2022)

print(car1.start_engine()) # Toyota Camry завел двигатель!

# Атрибуты объекта и атрибуты класса
# Атрибуты объекта
# Атрибуты объекта – это переменные, хранящие данные конкретного
# экземпляра класса.
# Они определяются в конструкторе __init__ и привязываются к объекту через
# self .
# Пример:
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand # Атрибут объекта
        self.model = model # Атрибут объекта
        self.year = year # Атрибут объекта

# Каждый объект ( car1 , car2 ) будет иметь свои собственные значения brand ,
# model и year .
# Атрибуты класса
# Атрибуты класса принадлежат всему классу, а не отдельному объекту. Они
# одинаковы для всех экземпляров.
# Пример:
class Car:
    wheels = 4 # Атрибут класса (количество колес у всех машин одинаковo)

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
# Мы можем обратиться к атрибуту класса через Car.wheels или car1.wheels , но
# изменять его для конкретного объекта нельзя.
# 🔹 Методы
# Методы – это функции, которые принадлежат классу и определяют его
# поведение. Они работают с атрибутами объекта или класса.
# Обычные методы (методы объекта)
# Такие методы принимают self как первый аргумент, что позволяет работать с
# атрибутами конкретного объекта.
# Пример:
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def start_engine(self):
        return f"{self.brand} {self.model} завел двигатель!" # Используем self.brand и self.model

# Методы класса ( @classmethod )
# Методы класса работают с атрибутами класса, а не конкретного объекта.
# Они получают cls (ссылку на сам класс) вместо self .
# Пример:
class Car:
    wheels = 4 # Атрибут класса

    @classmethod
    def set_wheels(cls, number):
        cls.wheels = number # Меняем атрибут класса

Car.set_wheels(6)
print(Car.wheels) # 6

# Статические методы ( @staticmethod )
# Статические методы не получают ни self , ни cls . Они ведут себя как обычные
# функции внутри класса и не зависят от конкретного объекта.
# Пример:
class Car:
    @staticmethod
    def car_info():
        return "Автомобиль — это средство передвижения."

print(Car.car_info()) # Автомобиль — это средство передвижения.

# 🔹 Итог
# Атрибуты объекта принадлежат конкретному объекту ( self.brand , self.model ).
# Атрибуты класса принадлежат всему классу ( wheels = 4 ).
# Методы объекта используют self и работают с данными конкретного
# экземпляра.
# Методы класса используют cls и работают с атрибутами класса.
# Статические методы ведут себя как обычные функции, но находятся
# внутри класса.
# Этот код покажет разницу между атрибутами и методами:


car1 = Car("Toyota", "Camry", 2023)
print(car1.start_engine()) # Toyota Camry завел двигатель!
print(Car.car_info()) # Автомобиль — это средство передвижения.