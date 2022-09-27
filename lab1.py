#Variant 5
#Ladoshin Maxim
#Task - Find S, V, R, r of a dodecaider

MAX_THRESHOLD = 1e+8

#calc function, return a tuple of format (S, V, R, r)
def calc(a):
    S = 3 * a**2 * (5 * (5 + 2*5**0.5))**0.5
    V = 0.25*a**3 * (15 + 7*5**0.5)

    R = 0.25 * a * (1 + 5**0.5)*3**0.5
    r = 0.25 * a * (10 + 22/5**0.5)**0.5

    return (S, V, R, r)

def printNum(string, num):
    print("{base}: {:,.2f}".format(num, base=string) if num < MAX_THRESHOLD else "{base}: {:,.2g}".format(num, base=string))
    
#User input
a = float(input("Введите длину ребра А для Додекаэдра: "))

out = calc(a)
S = out[0]
V = out[1]
R = out[2]
r = out[3]

printNum("\nПлощадь поверхности додекаэдра", S)
printNum("Объём додекаэдра", V)
printNum("Радиус описанной сферы додекаэдра", R)
printNum("Радиус вписанной сферы додекаэдра", r)


def test():
    print("\n<<Tests>>")
    arr = [(1, 20.65, 7.66, 1.40, 1.11), (2, 82.58, 61.30, 2.80, 2.23), (5, 516.14, 957.89, 7.01, 5.57)]
    count = 0
    epsilon = 0.5
    
    for dataBlock in arr:
        a = dataBlock[0]
        
        b = dataBlock[1]
        c = dataBlock[2]
        d = dataBlock[3]
        e = dataBlock[4]
        
        out = calc(a)

        if(abs(b - out[0])<epsilon and abs(c - out[1])<epsilon and abs(d - out[2])<epsilon and abs(e - out[3])<epsilon):
            print("Test {testCount} PASSED!".format(testCount=count))
        else:
            print("Test {testCount} FAILED! Input: {inp}".format(testCount=count, inp = a))

        count += 1


test()

        
    


