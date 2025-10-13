people = {
    "person1": {
        "firstname": "Alice",
        "lastname": "Johnson",
        "age": 28,
        "city": "New York"
    },
    "person2": {
        "firstname": "Bob",
        "lastname": "Miller",
        "age": 35,
        "city": "London"
    },
    "person3": {
        "firstname": "Charlie",
        "lastname": "Kim",
        "age": 30,
        "city": "Seoul"
    },
    "person4": {
        "firstname": "Diana",
        "lastname": "Lopez",
        "age": 25,
        "city": "Madrid"
    },
    "person5": {
        "firstname": "Ethan",
        "lastname": "Singh",
        "age": 32,
        "city": "Toronto"
    }
}

# for key in people.keys():
#     print(f"Below are the values for {key}")
#     for key, value in people[key].items():
#         print(f"\t{key} => {value}")
        
for key, value in people.items():
    print(f"Below are the values for {key}")
    for key, value in value.items():
        print(f"\t{key} => {value}")