# def get_number(ask_user):
#     print(ask_user)
#     if 'целое' or 'натуральное' and 'число' in ask_user:
#         return int(input())
#     elif 'любое число' in ask_user:
#         return float(input())
#     else:
#         return input()

###########################

import fibonacci as fibo
import getnumber as gn

with open('Result_fib.txt', 'w') as result:
    n = gn.get_number('Сколько чисел Фибоначчи нужно добавить (введите натуральное число): ')
    for e in range(1, n):
        result.write(f'{fibo.fib(e)}, ')
    result.write(f'{fibo.fib(n)}')

