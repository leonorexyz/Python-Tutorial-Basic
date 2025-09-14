'''
country_code = {
    "id": "indonesia",
    "us": "united stats",
    "jp": "japan",
    "my": "malaysia"
}

print(country_code["jp"])
print(len(country_code))

code = "kr"
check = code in country_code
print(check)

print(country_code.get(("kr"), "Data tidak ditemukan"))

country_code.update({"us":"united states"})
country_code.update({"kr":"korean"})
print(country_code)

del country_code["id"]
print(country_code)

for countries in country_code:
    print(countries)

for countries in country_code.keys():
    print(country_code.get(countries))

for countries in country_code.items():
    print(countries)

crc = country_code.copy()
print(crc)

country_code_pop = country_code.pop("my")
print(country_code_pop)
print(country_code)

country_code_pop = country_code.popitem()
print(country_code_pop)
print(country_code)
'''

import datetime

students = {
    "name": "Hengki",
    "nim": "535150015",
    "sks": 146,
    "ipk": 3.8,
    "tanggalLahir": datetime.date(1997, 8, 17)
}
students1 = {
    "name": "Hengki",
    "nim": "535150015",
    "sks": 146,
    "ipk": 3.8,
    "tanggalLahir": datetime.date(1997, 8, 17)
}
students2 = {
    "name": "Felix",
    "nim": "535150033",
    "sks": 146,
    "ipk": 3.3,
    "tanggalLahir": datetime.date(1997, 8, 17)
}
students3 = {
    "name": "Kevin",
    "nim": "535150038",
    "sks": 146,
    "ipk": 3,
    "tanggalLahir": datetime.date(1997, 8, 17)
}

studentsData = {
    "students1": students1,
    "students2": students2,
    "students3": students3
}

print(studentsData)

print(f"{'Key':<10} {'Name':<17} {'NIM':<9} {'SKS':<3} {'IPK':<4} {'Tanggal Lahir':<12}")
print("-"*60)

for student in studentsData:
    name = studentsData[student]["name"]
    nim = studentsData[student]["nim"]
    sks = studentsData[student]["sks"]
    ipk = studentsData[student]["ipk"]
    tanggalLahir = studentsData[student]["tanggalLahir"].strftime("%d-%m-%Y")
    print(f"{student:<10} {name:<17} {nim:<9} {sks:<3} {ipk:<4} {tanggalLahir:<12}")