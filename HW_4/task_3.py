# Задать натуральное число k.
# Сформируйте многочлен (полином) степени k со случайными коэффициентами из промежутка от 0 до 100, включительно.
# Многочлен вывести в консоль и записать в файл.


import random

k = int(input('Введите число k = '))
coef = [random.randint(-100, 100) for i in range(0, k + 1)]
print(coef)


def Polynom(k, coef):
    pol = ''
    for i in range(0, k + 1):
        if coef[i] == 0:
            pol = ''
        elif k - i > 1 and coef[i] != 0:
            pol += f'{coef[i]}*x^{k - i} + '
        elif k - i == 1 and coef[i] != 0:
            pol += f'{coef[i]}*x + '
        else:
            pol += f'{coef[i]} = 0'
    return pol


with open('pol.txt', 'w') as data:
    data.write(Polynom(k, coef).replace('+ -', '- '))