# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

day_num = int(input('Введите цифру от 1 до 7, обозначающую день недели: '))
# print(day_num in range(1, 6))
if day_num in range(1, 6):
    print('Нет')
else:
    print('Да')