def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1, 2, 3])
value_list = ['Крот', False, 75]
value_dict = {'a': True, 'b': 28, 'c': 'Rock'}
print_params(*value_list)
print_params(**value_dict)
value_list_2 = [(75, 38), False]
print_params(*value_list_2, 42)