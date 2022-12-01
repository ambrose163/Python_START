# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = input('Введите вещественное число n = ')
digit_sum = 0
for i in num:
    if i.isdigit():
        digit_sum += int(i)
print(f'Сумма цифр числа {num} равна {digit_sum}')


# count = 0
# for i in num:
#     if i == ".":
#         i = 0
#     count += int(i)
# print(count)9