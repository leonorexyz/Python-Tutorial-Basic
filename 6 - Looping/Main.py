# Looping - A way to iterate something
# for loop, for i in range(n), let's say n is 11 so it will iterate from 0-10, for loop is used when we know the range, you can also define the start step, end step (remember it's always n+1), and the step
# while loop, while loop is used when we don't know how much we want to iterate, it'll always loop until the condition break

'''
n = 10
result = 1
for i in range(0,n+1):
    if(i!=0):
        result *= i
print(result)
'''

'''
n = 5
for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()
'''

'''
n = 5
result = 1
while n: #if n is <1 the condition will break, remember in programming 1 = True, 0 = False
    result *= n
    n -= 1
print(result)
'''

'''
fact = int(input("Insert number : "))
result = 1
for i in range(fact,0,-1):
    result *= i
    if(i == 1):
        print(str(i)+ " = ",end="")
    else:
        print(str(i)+ " * ",end="")
print(result)
'''

# fast way to implement triangle star - exercise
print("Choose Shape".center(20,"-"))
print("1. Square")
print("2. Triangle")
print("3. Reverse Triangle")
print("4. Diamond")
shape = int(input("Choose shape : "))
size = int(input("Choose size : "))
if(shape == 1):
    for i in range(1, size+1):
        print("*" * size)
if(shape == 2):
    for i in range(1, size+1):
        print("*" * i)
if(shape == 3):
    for i in range(size, 0, -1):
        print("*" * i)
if(shape == 4):
    for i in range(1, size*2):
        print(" "*(size-(int(size)-abs(i-size))),end="")
        print("*"*(int(size)-abs(i-size)))
        print(" "*(size-(int(size)-abs(i-size))),end="")
        # print((int(size)-abs(i-size)))
        # print(size-(int(size)-abs(i-size)))
