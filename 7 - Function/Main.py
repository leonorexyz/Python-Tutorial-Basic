# Function - a way to write a subalgorithm that can be called from main function it also can pass parameters and return values
def rectangle(s):
    area = s ** 2
    return area

def triangle(s,t):
    area = 0.5*s*t
    return area

def circle(s):
    if(s%7==0):
        area = s * 22/7
    else:
        area = 3.14 * (s**2)
    return area

print(triangle(5,10))