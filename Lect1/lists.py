
numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]

numbers.append(6)
print(numbers) # [10, 2, 3, 4, 5, 6]

numbers.remove(3)
print(numbers) # [10, 2, 4, 5, 6]

del numbers[3]
print(numbers) # [10, 2, 4, 6]


##
list1 = [1,2,3,4,5,6]
list2 = list1

print(list1)
list2[0] = 12 # [1, 2, 3, 4, 5, 6]
print(list1) # [12, 2, 3, 4, 5, 6]
print(list2) # [12, 2, 3, 4, 5, 6]

list1.pop() # извлекает последний элемент
list1.pop(3) # извлекает 4ый элемент
list1.insert(3, 11) # вставить элемент 11 на 4ое место
list1.append(11) # добавить в конец списка 11