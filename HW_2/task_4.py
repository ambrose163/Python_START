# Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
# Найдите произведение элементов на индексах, хранящихся в файле indexes.txt (в одной строке один индекс).
# Решение должно работать при любом натуральном N.


n = int(input('Введите число n = '))

list_n = []
for i in range(-abs(n), abs(n) + 1):
    list_n.append(i)
print(list_n)

prod = 1
path = 'indexes.txt'
with open(path, 'r') as data:
    for line in data:
        prod *= list_n[int(line)]
    print(prod)