import os
os.system('cls')

import function as fn

expression = input('Введите числовое выражение: ')
components = expression.split()
multDiv = []

result = 0
for i in range(0, len(components) - 2, 2):
    if components[i + 1] == '*' or components[i + 1] == '/':
        result = fn.Operation(components[i], components[i + 1], components[i + 2])
        multDiv.append(str(result))
    else:
        multDiv.append(components[i])
        multDiv.append(components[i + 1])

print(multDiv)

# result1 = fn.Operation(multDiv[0], multDiv[1], multDiv[2])
# for i in range(3, len(multDiv) - 2, 2):
#     result1 = fn.Operation(str(result1), components[i + 1], components[i + 2])

# print(f'Ответ: {result1}')


