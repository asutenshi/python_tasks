# Вариант 5

equation = input('Введите уравнение вида x+5=2 или 5+x=2: ')
for x in range(-9, 18):
    if equation[0] == 'x': 
        if x + int(equation[1:3]) == int(equation[-1]): print(x)
    else:
        if equation[1] == '+':
            if int(equation[0]) + x == int(equation[-1]): print(x)
        else:
            if int(equation[0]) - x == int(equation[-1]): print(x)
