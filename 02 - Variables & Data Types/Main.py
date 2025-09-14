# Variables - you can store something at a variable
x = 3
y = 2
z = x + y
print(z)

pi = 3.14
r = 5
area = pi * r**2 #this is an area of a circle, the ** operator is power in python
print(area)

idol1 = "Moona Hoshinova"
idol2 = "Kureiji Ollie"
idol3 = "Kobo Kanaeru"
idols = idol1 + idol2 + idol3 #you can also add several string to a variable
print(idols)

# Data Types - there are different data types used in python the most common one are integer, float, string, and boolean
a = 1 #integer
b = 3.14 #float
c = "Luna" #string
d = False #boolean
print(type(a)) #this is how you print the data type
print(type(b))
print(type(c))
print(type(d))

# Casting - ways to convert data types
a = 1
b = "1"
c = a+int(b)
print(c)