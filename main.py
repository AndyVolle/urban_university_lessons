def test(*args):
    for arg in args:
        print(arg)


test('С наступающим новым', 2024, 'годом', {'int': 3, 'str': 'cnh 4', 'bool': True}, [3, 'cnh 4', True])


def factorial(n):
    if n != 1:
        factorial_n_minus_1 = factorial(n=n - 1)
        return factorial_n_minus_1 * n
    else:
        return 1


user_value = input('Введите значение для вычисления факториала:')
test(f'{user_value}!={factorial(int(user_value))}')
