# Задайте список случайных чисел. Выведите:
# а) список чисел, которые не повторяются в заданном списке,
# б) список повторяемых чисел,
# в) список без повторений


lst = [1, 2, 3, 5, 1, 5, 3, 10]
lst_1 = []
lst_2 = []
for num in lst:
    if lst.count(num) == 1:
        lst_1.append(num)
    else:
        if lst_2.count(num) == 0:
            lst_2.append(num)

lst_3 = list(set(lst))

print(lst_1)
print(lst_2)
print(lst_3)