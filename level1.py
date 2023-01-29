import os
os.system('cls')

def IfNumber(line):
    array = list(line)
    for element in array:
        if ord(element) < 48 or ord(element) > 57:
            return False
    return True

def IfArithmeticSign(symbol):
    if len(symbol) != 1:
        return False
    else:
        if ord(symbol) != 42 and ord(symbol) != 43 and ord(symbol) != 45 and ord(symbol) != 47:
            return False
    return True

def GetNameOfOperation(symbol):
    if IfArithmeticSign(symbol):
        if symbol == '+':
            return 'сложения'
        elif symbol == '-':
            return 'вычитания'
        elif symbol == '*':
            return 'умножения'
        elif symbol == '/':
            return 'деления'
    else:
        return 'несуществующий символ'
        

def Operation(a, b, c):
    if IfNumber(a) and IfNumber(c) and IfArithmeticSign(b):
        if b == '+':
            return(int(a) + int(c))
        elif b == '-':
            return(int(a) - int(c))
        elif b == '*':
            return(int(a) * int(c))
        elif b == '/':  
            return(int(a) / int(c))
    else:
        return 'Некорректный ввод данных. Повторите попытку'

expression = input('Введите числовое выражение,\n'
                    'состоящее из двух чисел и одного действия: ')
components = expression.split()
operation = GetNameOfOperation(components[1])
print(f'Вы ввели числа: {components[0]} и {components[2]}.')
print(f'Результат {operation}:')
print(Operation(components[0], components[1], components[2]))
