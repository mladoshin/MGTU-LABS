import math as m
SIZE = 160
eps = float(input("Enter a eps: "))
             
for y in range(int(SIZE//2), int(-SIZE//2-1), -1):
    for x in range(int(-SIZE//2), int(SIZE//2+1)):
        if(abs(int(y) - SIZE//2*m.sin(x/((SIZE/2) / m.pi))) <= eps):
            print("*", end='')
        elif x== 0:
            print('|', end='')
            continue
        elif y == 0:
            print('-', end='')
            continue
        else:
            print(" ", end='')
    print()


    #comment

