fav_languages = {
    "Alice": "Python",
    "Bob": "Java",
    "Charlie": "C++",
    "Diana": "JavaScript",
    "Ethan": "Go",
    "Fiona": "Ruby",
    "George": "C#",
    "Hannah": "TypeScript",
    "Ian": "Rust",
    "Julia": "Kotlin"
}

people = ["Alice", "Bob", "Kevin", "Julia", "Sara", "George", "Liam", "Hannah", "Zoe", "Charlie"]

for value in people:
    if value in fav_languages.keys():
        print(f"{value} your favourite language is {fav_languages[value]}")
    else:
        print(f"{value} you will have to take the poll first...")