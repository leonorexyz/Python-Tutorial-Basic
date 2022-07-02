'''
# Basic String Manipulation
name = "Test" 
length = len(name) #counting length of a string variable
existsCharacter = "st" in name #check on the condition of a pattern exists in a string variable
notExistsCharacter = "s" not in name #check on the condition of a pattern not exists in a string variable
nameRepetition = name * 10 #string multiplication operator can be used to repeat a string n-times
index1 = name[0] #to get the first index of a string variable
index3 = name[2] #to get the third index of a string variable
index345 = name[4:7] #to get the third - fifth index of a string variable
indexReverse = name[-1] #to get the first index from the end of a string variable
indexEven = name[1:len(name):2] #to get the even index of a string variable
ascii_code = ord("a") #to get the ascii code of 'a' character
print(length)
print(existsCharacter)
print(notExistsCharacter)
print(nameRepetition)
print(indexReverse)
print(indexGenap)
print(min(name)) #to get the minimum character of a string variable
print(max(name)) #to get the maximum character of a string variable
print(ascii_code)
print(name.count("t")) #to count a pattern of a string variable
print(name.upper()) #to capitalize all string of a string variable
print(name.lower()) #to decapitalize all string of a string variable
print(name.isupper()) #to check is all string is capitalized in a string variable
print(name.islower()) #to check is all string is decapitalized in a string variable
print(name.isalpha()) #to check is all string is text in a string variable
print(name.isalnum()) #to check is all string is number & text in a string variable
print(name.isdecimal()) #to check is all string is number in a string variable
print(name.isspace()) #to check is all string is space / tab in a string variable
print(name.istitle()) #to check is the first letter of a string is capitalized in a string variable
'''

'''
# Advanced String Manipulation
title = "Mantra Hujan"
print(title.startswith("Mantra")) #to check a string variable is started with a following pattern
print(title.endswith("Hujan")) #to check a string variable is ended with a following pattern

gen1 = ['Moona', 'Risu', 'Iofi']
gen2 = ",".join(gen1) #to join a string from a list
gen3 = gen2.split(",") #to split a string to a list
print(gen1)
print(gen2)
print(gen3)

gen1 = "Moona".rjust(20,"-") #to set the offset on the right side with the following string
print(gen1)

gen1 = "Moona".ljust(20,"-") #to set the offset on the left side with the following string
print(gen1)

gen1 = "Moona".center(20,"-") #to set the offset on the center with the following string
print(gen1)
'''

number = 2003.1573 
percentage = 0.4571
number1 = 10
number2 = 5
print(f"number : {number}") #to print format an integer without having to cast it to a string
print(f"number : {number:,}") #to add a group sepator
print(f"number : {number:.2f}") #to format the decimal with 2 precision digits
print(f"Percentage : {percentage:.2%}") #to format the percentage with 2 precision digits
print(f"Hasil Perkalian : {number1*number2}") #to calculate inside a print format
