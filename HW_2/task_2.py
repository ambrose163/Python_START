# Напишите программу, которая принимает на вход натуральное число N и выдает список факториалов по основаниям от 1 до N


n = int(input('Введите целое число n = '))

print()
list_fact = []

def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n


for i in range(1, n + 1):
    list_fact.append(fact(i))

print(list_fact)