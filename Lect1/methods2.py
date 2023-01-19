# new file function_file.py

import function_file
print(function_file.f(1)) # Целое
print(function_file.f(2.3)) # 23
print(function_file.f(28)) # None


import function_file as ff
print(ff.f(1)) # Целое
print(ff.f(2.3)) # 23
print(ff.f(28)) # None


def new_string(symbol, count = 3): # определение изначального значения параметра функции позволяет не указывать ее в передаче
    return symbol * count

print(new_string('!', 5)) # !!!!!
print(new_string('!')) # !!!
print(new_string(4)) # 12


def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError: ...