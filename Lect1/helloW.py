print('hello мир')
a = 345
b = 2.1
n = 'petya \nthinking' # переход на новую строку \n
value = None
print(a, b, n)
print(type(a),type(b),type(value)) # комментарии через решётку

print(f'{a} - {b} - {n}')
print('{} - {} - {}'.format(a, b, n))
print('{1} - {2} - {0}'.format(a, b, n)) # меняет порядок вывода
print(a, '-', b, '-', n)
list = []
list2 = [1, 2, 3]
print(list, list2)

print('введите а')
a1 = input() # строковый тип
print('введите b')
b1 = input()
print(f'{a1} - {b1}')

print('введите c')
c = int(input()) # целочисленный тип
print('введите d')
d = int(input())

print(f'{c} + {d} = {c + d}')