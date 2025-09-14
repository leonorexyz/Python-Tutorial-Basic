#List / Array - a way to store more than one variable

list_numbers = [1,2,3,4,5]
print(list_numbers)
print(type(list_numbers))

list_strings = ["Raiden Shogun", "Venti", "Zhongli"]

list_boolean = [True,True,True,False]

list_combined = ["Luna",1,True]
print(list_combined)

list_students = [["Luna",1,True],["Raiden",2,False]]
print(list_students[-1][0])

list_100_even_numbers = list(range(2,101,2))
print(list_100_even_numbers)

list_100_square_numbers = [i**2 for i in range(1,101)]
print(list_100_square_numbers)

list_100_even_numbers_with_if = [i for i in range(2,101) if i%2==0]
print(list_100_even_numbers_with_if)
print(len(list_100_even_numbers_with_if))

list_students.append(["Venti",4,False])
print(list_students)

list_students.insert(2,["Sara",3,False])
print(list_students)

list_new_students = [["Ayaka",5,True],["Hu Tao",6,True]]
list_students.extend(list_new_students)
print(list_students)

list_students[-1][0] = "Thoma"
print(list_students)

list_students.remove(["Ayaka",5,True])
print(list_students)

list_students.pop()
print(list_students)

nilai = [96, 100, 100, 100, 100, 98]
print(nilai.count(100))
print(list_100_even_numbers_with_if.index(56))
nilai.sort()
print(nilai)
nilai.reverse()
print(nilai)
nilai_copy = nilai.copy()
print(nilai_copy)

# Data Enumeration
data_list = ["Luna","Raiden","Zhongli","Venti"]
for index, data in enumerate(data_list):
    print(f"Index ke-{index} adalah {data}")


