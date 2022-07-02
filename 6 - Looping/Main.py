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