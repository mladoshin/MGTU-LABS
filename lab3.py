#Написать программу, которая по введенным целочисленным
#координатам трех точек на плоскости вычисляет длины сторон
#образованного треугольника и длину высоты, проведенной из
#наибольшего угла.
#Определить, является ли треугольник остроугольным.
#Далее вводятся координаты точки. Определить, находится ли
#точка внутри треугольника. Если да, то найти расстояние от точки
#до ближайшей стороны треугольника.

#Maxim Ladoshin IU7-11B

import math as m
eps = 1e-5

#User Input
points = []   # A, B, C

for i in range(3):
    x, y = map(int, input("Введите координаты x, y точки {} через пробел: ".format(i+1)).split())
    point = (x, y)
    points.append(point)

print(points)

s_ab = ((points[0][0] - points[1][0])**2 + (points[0][1] - points[1][1])**2)**0.5     # find AB
s_bc = ((points[1][0] - points[2][0])**2 + (points[1][1] - points[2][1])**2)**0.5     # find BC
s_ac = ((points[0][0] - points[2][0])**2 + (points[0][1] - points[2][1])**2)**0.5     # find AC

print("Длина первой стороны AB: {:.5g}\nДлина второй стороны BC: {:.5g}\nДлина третьей стороны AC: {:.5g}".format(s_ab, s_bc, s_ac))

angle_a = m.acos((s_ab**2 + s_ac**2 - s_bc**2)/(2*s_ab*s_ac))

angle_b = m.acos((s_bc**2 + s_ab**2 - s_ac**2)/(2*s_bc*s_ab))

angle_c = m.pi - angle_a - angle_b

h = 0

if(s_ab >= s_bc and s_ab >= s_ac):
    # angle_c is the largest
    # ac*sinA
    h = s_ac*m.sin(angle_a)
elif(s_bc >= s_ab and s_bc >= s_ac):
    # angle_a is the largest
    # ab*sinb
    h = s_ab*m.sin(angle_b)
else:
    # angle_b is the largest
    # ab*sinA
    h = s_ab*m.sin(angle_a)

print("Высота проведенная из наибольшего угла: {:.5g}".format(h))

if(abs(angle_a - m.pi/2) < eps and abs(angle_b - m.pi/2) < eps and abs(angle_c - m.pi/2) < eps):
    print("Этот треугольник остроугольный")
else:
    print("Этот треугольник не остроугольный!")
#Calculations

p_x, p_y = map(float, input("Введите координаты x, y произвольной точки через пробел: ").split())

AB = (points[1][0] - points[0][0], points[1][1] - points[0][1])   # vector AB
BC = (points[2][0] - points[1][0], points[2][1] - points[1][1])   # vector BC
AC = (points[0][0] - points[2][0], points[0][1] - points[2][1])   # vector AC

PA = (points[0][0] - p_x, points[0][1] - p_y)                     # vector PA
PB = (points[1][0] - p_x, points[1][1] - p_y)                     # vector PB
PC = (points[2][0] - p_x, points[2][1] - p_y)                     # vector PC

a = PA[0]*AB[1] - PA[1]*AB[0]                                     # cross product of PA and AB
b = PB[0]*BC[1] - PB[1]*BC[0]                                     # cross product of PB and BC
c = PC[0]*AC[1] - PC[1]*AC[0]                                     # cross product of PC and AC

if(a > 0 and b > 0 and c > 0 or a < 0 and b < 0 and c < 0):
    print("Точка P({}, {}) лежит внутри треугольника".format(p_x, p_y))

    h1 = abs(a)/s_ab
    h2 = abs(b)/s_bc
    h3 = abs(c)/s_ac

    print("Кратчайшее растояние от точки P({}, {}) до стороны угла равно: {}".format(p_x, p_y, min(h1, h2, h3)))
else:
    print("Точка P({}, {}) не лежит внутри треугольника!".format(p_x, p_y))
#Output


