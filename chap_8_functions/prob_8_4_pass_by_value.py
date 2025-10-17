list_of_names = ["Harsh", "Drake", "Dragon", "Amber"]

def greet_names_list(name_list):
    count = len(name_list) - 1
    while count >= 0:
        name_list[count] = f"Hello {name_list[count]}! How are you?"
        count -= 1
    return name_list

print("before modification\n")
print(list_of_names)
new_list = greet_names_list(list_of_names[:])
print("\nafter modification\n")
print(f"Original list: {list_of_names}\n")
print(f"Modified list: {new_list}")