'''
# Branching - A way to decide an argument / decision
number = int(input("Masukkan number : "))
if(number % 2 == 0):
    print("This is an even number")
else:
    print("This is an odd number")

marks = 90
if(marks >= 80):
    print("A")
elif(marks >= 70):
    print("B")
elif(marks >= 56):
    print("C")
elif(marks >= 40):
    print("D")
else:
    print("E")
'''

#  Exercise - Simple Calculator
number1 = int(input("Insert number 1 : ")) #operand
operator = input("Insert operator : ")
number2 = int(input("Insert number 2 : "))

if(operator == "+"):
    print(f"Result : {number1+number2}")
if(operator == "-"):
    print(f"Result : {number1-number2}")
if(operator == "*"):
    print(f"Result : {number1*number2}")
if(operator == "/"):
    print(f"Result : {number1/number2}")

