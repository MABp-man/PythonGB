original = 1234
inverted = 0
while original != 0:
    print(inverted)
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('и наконец-то: ', inverted)


for i in 1,2,3,4,5:
    print(i**2)

list = [5,4,3,2,1]
for i in list:
    print(i*10)

r = range(2,11,2) # начало - конец - шаг, не забывать, что конец "не включая"
for i in r:
    print(i)

for i in 'fsdfg': # по всем буквам
    print(i)

