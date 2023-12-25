# Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2)
print_params(3, '4')
print_params(c=False)
print_params(b=25)
print_params(c=[1, 2, 3])

# Распаковка параметров:

values_list = [2, 'вторая строка', False]
values_dict = {'a': 3, 'b': 'третья строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры:

values_list_2 = [10, 'какая-то строка']
print_params(*values_list_2, 42)
