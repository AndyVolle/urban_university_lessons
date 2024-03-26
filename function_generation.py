# ============================== Задача 1 ==============================
print('=' * 30, 'Задача 1', '=' * 30)


# Задача 1: Фабрика Функций Написать функцию, которая возвращает различные математические функции (например, деление,
# умножение) в зависимости от переданных аргументов.

def operation_factory(operation):
    if operation == 'умножение':
        return lambda x, y: x * y
    elif operation == 'деление':
        return lambda x, y: x / y if y != 0 else 'Ошибка: деление на ноль'


multiply = operation_factory('умножение')
print(multiply(2, 3))

divide = operation_factory('деление')
print(divide(10, 2))
print(divide(10, 0))

# ============================== Задача 2 ==============================
print('=' * 30, 'Задача 2', '=' * 30)
# Задача 2: Лямбда-Функции Использовать лямбда-функцию для реализации простой операции и написать такую же функцию с
# использованием def. Например, возведение числа в квадрат

# Лямбда-функция
square = lambda x: x ** 2
print(square(5))  # Вывод: 25


# Функция с использованием def
def square_def(x):
    return x ** 2


print(square_def(5))

# ============================== Задача 3 ==============================
print('=' * 30, 'Задача 3', '=' * 30)


# Задача 3: Вызываемые Объекты Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__,
# который возвращает площадь прямоугольника, то есть a*b.

class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


a, b = 3, 4
rect = Rect(a, b)
print(f'Стороны: {a}, {b}')
print(f'Площадь: {rect()}')

# Результат:
# ============================== Задача 1 ==============================
# 6
# 5.0
# Ошибка: деление на ноль
# ============================== Задача 2 ==============================
# 25
# 25
# ============================== Задача 3 ==============================
# Стороны: 3, 4
# Площадь: 12