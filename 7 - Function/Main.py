# Function - a way to write a subalgorithm that can be called from main function it also can pass parameters and return values

def square(l):
    area = l ** 2
    return area

def triangle(l,h):
    area = 0.5*l*h
    return area

def circle(r):
    if(r%7==0):
        area = (r**2) * 22/7
    else:
        area = 3.14 * (r**2)
    return area

def rectangle(l,w):
    area = l * w 
    return area

def trapezoid(a,b,h):
    area = (a+b)*h/2
    return area

def pararellogram(l,h):
    area = l*h
    return area

def rhombus(d1,d2):
    area = d1*d2/2
    return area

def kite(d1,d2):
    area = d1*d2/2
    return area

while True:
    print("Choose Shape".center(20,"-"))
    print("1. Square")
    print("2. Triangle")
    print("3. Circle")
    print("4. Rectangle")
    print("5. Trapezoid")
    print("6. Pararellogram")
    print("7. Rhombus")
    print("8. Kite")
    shape = int(input("Choose shape : "))
    if(shape == 1):    
        length = int(input("Insert length : "))
        print(square(length))
    elif(shape == 2):    
        length = int(input("Insert length : "))
        height = int(input("Insert height : "))
        print(triangle(length,height))
    elif(shape == 3):    
        radius = int(input("Insert radius : "))
        print(circle(radius))
    elif(shape == 4):    
        length = int(input("Insert length : "))
        width = int(input("Insert width : "))
        print(rectangle(length,width))
    elif(shape == 5):    
        a = int(input("Insert top length : "))
        b = int(input("Insert bottom length : "))
        height = int(input("Insert height : "))
        print(trapezoid(a,b,height))
    elif(shape == 6):    
        length = int(input("Insert length : "))
        height = int(input("Insert height : "))
        print(pararellogram(length,height))
    elif(shape == 7):    
        d1 = int(input("Insert diameter 1 : "))
        d2 = int(input("Insert diameter 2 : "))
        print(rhombus(d1,d2))
    elif(shape == 8):    
        d1 = int(input("Insert diameter 1 : "))
        d2 = int(input("Insert diameter 2 : "))
        print(kite(d1,d2))

    decision = input("Do you want to use program again (Y/N) ? ")
    if(decision == "N"):
        break