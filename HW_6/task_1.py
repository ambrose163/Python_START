# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# По возможности реализуйте использования скобок, меняющих приоритет операций.


user_input = [element for element in input("Введите арифметическое выражение\n").split()]
components = [int(element) if element.isdigit() else element for element in user_input]

result = 0
while '/' in components:
    i = components.index('/')
    result = components[i - 1] / components[i + 1]
    components = components[:i - 1] + [result] + components[i + 2:]
while '*' in components:
    i = components.index('*')
    result = components[i - 1] * components[i + 1]
    components = components[:i - 1] + [result] + components[i + 2:]
while '+' in components:
    i = components.index('+')
    result = components[i - 1] + components[i + 1]
    components = components[:i - 1] + [result] + components[i + 2:]
while '-' in components:
    i = components.index("-")
    result = components[i - 1] - components[i + 1]
    components = components[:i - 1] + [result] + components[i + 2:]

print(components)