rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Ganges": "India",
    "Yangtze": "China",
    "Mississippi": "United States",
    "Danube": "Germany",
    "Thames": "United Kingdom",
    "Volga": "Russia",
    "Mekong": "Vietnam",
    "Tigris": "Iraq"
}

for key, value in rivers.items():
    print(f"The {key} flows through {value}")

print()
for key in rivers.keys():
    print(key, end=", ")

print()
for value in rivers.values():
    print(value, end=", ")