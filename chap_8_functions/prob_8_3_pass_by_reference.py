list_of_names = ["Harsh", "Drake", "Dragon", "Amber"]

def greet_names_list(name_list):
    count = len(name_list) - 1
    while count >= 0:
        name_list[count] = f"Hello {name_list[count]}! How are you?"
        count -= 1

print(list_of_names)
greet_names_list(list_of_names)
print("after modification\n")
print(list_of_names)