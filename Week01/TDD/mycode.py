def hello_world():
    return 'hello world'

def create_num_list(length):
    return [x for x in range(length)]

def custom_func_x(x, const, power):
    return const * (x) ** power

def custom_non_lin_num_list(length, const, power):
    return [custom_func_x(x, const, power) for x in range(length)]

def sum_two_numbers(x, y):
    return x + y

def is_even(x):
    return x % 2 == 0