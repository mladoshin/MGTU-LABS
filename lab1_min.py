#Variant 5
#Ladoshin Maxim IU7-11B
#Task - Find S, V, R, r of a dodecaider
    
a = float(input("Введите длину ребра А для Додекаэдра (a - положительное): "))       #User input

if a >= 0:                                               #Check if an edge of dodecaider has a positive length
    S = 3 * a**2 * (5 * (5 + 2*5**0.5))**0.5              #Find volume
    V = 0.25*a**3 * (15 + 7*5**0.5)                       #Find surface area
    R = 0.25 * a * (1 + 5**0.5)*3**0.5                    #Find R
    r = 0.25 * a * (10 + 22/5**0.5)**0.5                  #Find r

    #Output
    print("\nПлощадь поверхности додекаэдра: {:,.5g}".format(S))
    print("Объём додекаэдра: {:,.5g}".format(V))
    print("Радиус описанной сферы додекаэдра: {:,.5g}".format(R))
    print("Радиус вписанной сферы додекаэдра: {:,.5g}".format(r))
else:                                                     #print a message if the value of a is lt 0
    print("Невалидное значение!")
