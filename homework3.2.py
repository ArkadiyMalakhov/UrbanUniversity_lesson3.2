def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [33, 34, 35])


def print_params(*args):
    print(*args)


print_params(True, 'Один', 2, 3)
print_params()


def print_params(a, b, c, d, e, g):
    print(a, b, c, d, e, g)


values_list = [False, 'Пять', 6]
values_dict = {'d': True, 'e': 400, 'g': 'Пятьсот'}
print_params(*values_list, **values_dict)


def print_params(*values_list_2):
    print(*values_list_2)


values_list_2 = ['Сто', 200]
print_params(*values_list_2, 300)
