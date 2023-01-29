import os
os.system('cls')

import function as fn

expression = input('Введите числовое выражение из действий одной ступени: ')
components = expression.split()
result = fn.Operation(components[0], components[1], components[2])
for i in range(3, len(components) - 1, 2):
    result = fn.Operation(str(result), components[i], components[i + 1])

print(f'Ответ: {result}')
