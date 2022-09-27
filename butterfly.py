# Find if a point lies within a butterfly
# Maxim Ladoshin IU7-11B

import math as m

#User input
x, y = map(float, input("Введите координаты точки x и y через пробел: ").split())

f1 = -1/8*(x+9)**2 + 8
f2 = -1/8*(x-9)**2 + 8
f3 = 7*(x+8)**2 + 1
f4 = 7*(x-8)**2 + 1
f5 = 1/49 * (x+1)**2
f6 = 1/49*(x-1)**2

#bottom
f7 = -1/16*x**2
f8 = 2.8 * m.cos(m.pi/5*x)-4.2

if( -9 <= x <= -1):
    if(y <= f1 and y >= f5 and y >= f3):
        print("Верхнее левое крыло!")
    elif(y <= f7 and y >= f8):
        print("Нижнее лувое крыло")
    
elif(-1 <= x <= 1):
    pass
elif(1 <= x <= 9):
    print(y)
    print(f2, f6, f4)
    if(y <= f2 and y >= f6):
        if(x >= 8 and y >= f4 or x < 8):
            print("Верхнее правое крыло!")
            
    elif(y <= f7 and y >= f8):
        print("Нижнее правое крыло")
    

