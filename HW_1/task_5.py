# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Результат округлить до сотых.

# point_A = [7, -5]
# point_B = [1, -1]
#
# distance = ((point_B[0] - point_A[0]) ** 2 + (point_B[1] - point_A[1]) ** 2) ** 0.5
# print(f'distance = {round(distance, 2)}')
# -----------------------------------------

point_A = input('Введите координаты точки А x,y = ')
point_B = input('Введите координаты точки В x,y = ')
xA = int(point_A.split(',')[0])
yA = int(point_A.split(',')[1])
xB = int(point_B.split(',')[0])
yB = int(point_B.split(',')[1])

distance = ((xB - xA) ** 2 + (yB - yA) ** 2) ** 0.5
print(f'distance = {round(distance, 2)}')