group1 = {
    "Alice": "Python",
    "Bob": "Java",
    "Charlie": "C++",
    "Diana": "JavaScript",
    "Ethan": "Go"
}

group2 = {
    "Fiona": "Ruby",
    "George": "C#",
    "Hannah": "TypeScript",
    "Ian": "Rust",
    "Julia": "Kotlin"
}

group3 = {
    "Kevin": "Swift",
    "Laura": "PHP",
    "Mike": "Scala",
    "Nina": "Perl",
    "Oscar": "Elixir"
}

all_groups = [group1, group2, group3]

for group in all_groups:
    for key, value in group.items():
        print(f"{key}: {value}")