from itertools import count


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