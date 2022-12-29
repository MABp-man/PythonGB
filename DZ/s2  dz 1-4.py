# метод получения числа от пользователя с уточнением типа в запросе

def get_number(ask_user):
    print(ask_user)
    if 'целое' or 'натуральное' and 'число' in ask_user:
        return int(input())
    elif 'любое число' in ask_user:
        return float(input())
    else:
        return input()

# метод вычисления факториала

def factorial(num):
    f = 1
    while num > 1:
        f = f * (num-1)
        num -= 1
    return f

# Задача 1. Напишите программу, которая принимает на вход число N
# и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = get_number('Введите натуральное число')
factorials = list(range(1, N+1))
while N > 1:
    factorials[N-1] *= factorial(N)
    N -= 1
print(factorials)

# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

print('\n X  |  Y  |  Z  | ¬(X ∧ Y) ∨ Z')
print('==============================')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            if not(x and y) or z == 1:
                print(f' {x}  |  {y}  |  {z}  |     {1}')
            else:
                print(f' {x}  |  {y}  |  {z}  |     {0}')


# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

print()
s1 = 'one'
s2 = 'onetwonine'
for i in s1:
    count = 0
    for j in s2:
        if i == j:
            count += 1
    print(f'{i} - {count}')

# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

N4 = get_number('Введите натуральное число')
list_n = list(range(-N4, N4+1))
print(list_n)
list_n[0:1] = [list_n[-2], list_n[-1], list_n[0]]
del list_n[-2:]
print(list_n)
