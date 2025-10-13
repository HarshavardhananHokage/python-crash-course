person = {
    "first_name": "Jackie",
    "last_name": "Chan",
    "age": 70,
    "city": "Hong Kong"
}

print(f"Name is: {person.get("first_name")} {person.get("last_name")}")
print(f"Their age is: {person.get("age")}")
print(f"Their current city is: {person.get("city")}")