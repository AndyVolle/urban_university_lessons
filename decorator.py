# Задание:
# Напишите 2 функции:
# Функция которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и
# "Составное" в противном случае.
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # проверка результата сложения на простое число (число является простым, если оно больше 1 и при этом делится
        # без остатка только на 1 и на самого себя)
        if result > 1:
            for i in range(2, result):
                if (result % i) == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)

# Результат:
# Простое
# 11