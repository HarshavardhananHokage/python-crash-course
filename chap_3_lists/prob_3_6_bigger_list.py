invite_list = ['Alexander', 'Genghis Khan', 'Lee Kuan Yew']

print("People! I found a bigger table. So inviting additional people to the dinner. The more the merrier and some thunder too!\n")

invite_list.insert(0, "Nicola Tesla")
invite_list.insert(2, "Teddy Roosevelt")
invite_list.append("Zeus")
invite_list.append("Thor")

for person in invite_list:
    print(f"Welcome to my thunderous dinner: {person}")