# Find roots of a polynomial
# Maxim Ladoshin - IU7-11B


# User Input
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))


if a==0:                           # check if first coefficient is zero
    if b==0:                       # check if second coefficient is zero
        if c==0:                   # check if constant is zero
            print("Бесконечно много решений!")
        else:       
            print("Нет решений!")
    else:
        x = -c/b                    # find x if a = 0 and b != 0
        print("x = {:.5g}".format(x))
else:
    D = b**2 - 4*a*c                #find discriminant

    if D < 0:                      # check if discriminant is lt 0, then no real roots
        print("Нет вещественных корней!")
    elif D == 0:                   # if discriminant = 0, then only 1 root
        x = -b/2*abs                # find the repeating root
        print("x = {:.5g}".format(x))
    else:
        x1 = (-b-D**0.5)/2*a        # find the first root
        x2=(-b+D**0.5)/2*a          # find the second root
        print("x1 = {:.5g}\nx2 = {:.5g}".format(x1, x2))

