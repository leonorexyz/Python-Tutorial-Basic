# Function - a way to write a subalgorithm that can be called from main function it also can pass parameters and return values
'''
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
'''

# args - multiple parameters
'''
def sumOfNumber(*data):
    sum = 0
    for x in data:
        sum += x
        print(sum)

sumOfNumber(1,2,3,4,5)
'''
'''
# kwargs - multiple parameters with key value pair
def personDetail(**data):
    for key,value in data.items():
        print(f"{key} : {value}")

personDetail(name="John",age=20,city="New York")
personDetail(name="Doe",age=25,city="Los Angeles",job="Engineer")
'''

'''
# combine args and kwargs
def math(*nums, **operator):
    result = 0
    if(operator["operation"] == "add"):
        for x in nums:
            result += x
    elif(operator["operation"] == "subtract"):
        result = nums[0]
        for x in nums[1:]:
            result -= x
    elif(operator["operation"] == "multiply"):
        result = 1
        for x in nums:
            result *= x
    elif(operator["operation"] == "divide"):
        result = nums[0]
        for x in nums[1:]:
            result /= x
    return result

result = math(1,2,3,4,5,operation="add")
print(result)
'''

# lambda function - a function that can be written in one line
# syntax : lambda parameters : expression
square = lambda x : x**2
print(square(5))

power = lambda x, y : x**y
print(f"2^3 = {power(2,3)}")

# lambda example list sorting
# sorting without lambda
names = ["John", "Doe", "Alice", "Bob"]
def nameLength(name):
    return len(name)

names.sort(key=nameLength)
print(names)

# sorting with lambda
names = ["John", "Doe", "Alice", "Bob"]
names.sort(key=lambda name: len(name))
print(names)

# lambda filter
numbers = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = list(filter(lambda x: x%2==0, numbers))
print(evenNumbers)

# lambda with curried function
def square(n):
    return lambda x: x**n

square2 = square(2)
square3 = square(3)
print(square2(5)) # 5^2
print(square3(5)) # 5^3
print(square(4)(5)) # 5^4