# Написать программу по переводу целого числа из десятичной системы счисления в двоичную.


def decimal_to_binary(decimal):
    binary = str(decimal % 2)
    while decimal // 2 != 0:
        decimal = decimal // 2
        binary = str(decimal % 2) + binary
    return binary


print(decimal_to_binary(46))
print(decimal_to_binary(2))