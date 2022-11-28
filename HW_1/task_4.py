# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
# в этой четверти (x и y).

import random

quad = random.randint(1, 4)
print(quad)
if quad == 1:
    print('x > 0 and y > 0')
elif quad == 2:
    print('x < 0 and y > 0')
elif quad == 3:
    print('x < 0 and y < 0')
else:
    print('x > 0 and y < 0')