# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

print(' X  |  Y  |  Z  | ¬(X ∧ Y) ∨ Z')
print('==============================')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            if not(x and y) or z == 1:
                print(f' {x}  |  {y}  |  {z}  |     {1}')
            else:
                print(f' {x}  |  {y}  |  {z}  |     {0}')
