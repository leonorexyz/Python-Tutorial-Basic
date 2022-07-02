# Looping - A way to iterate something
# for loop, for i in range(n), let's say n is 11 so it will iterate from 0-10, for loop is used when we know the range
# while loop, while loop is used when we don't know how much we want to iterate, it'll always loop until the condition break

n = 10
result = 1
for i in range(11):
    if(i!=0):
        result *= i
print(result)

n = 6
for i in range(n):
    for j in range(i):
        print("*", end=" ")
    print()

n = 5
result = 1
while n: #if n is <1 the condition will break, remember in programming 1 = True, 0 = False
    result *= n
    n -= 1
print(result)
