invite_list = ['Alexander', 'Genghis Khan', 'Lee Kuan Yew']

print("People! I found a bigger table. So inviting additional people to the dinner. The more the merrier and some thunder too!\n")

invite_list.insert(0, "Nicola Tesla")
invite_list.insert(2, "Teddy Roosevelt")
invite_list.append("Zeus")
invite_list.append("Thor")

for person in invite_list:
    print(f"Welcome to my thunderous dinner: {person}")

print("\nThe dinner table won't be arriving on time. So I can only invite 2 people. I will have to uninvite the others. I am a bad host!\n")

list_length = len(invite_list)

while list_length > 2:
    print(f"Sorry. Will have to uninvite you {invite_list.pop()}. Will organize a better dinner next time.")
    list_length = len(invite_list)

print()
for person in invite_list:
    print(f"Welcome to my average dinner: {person}")

print("\nTable has broken. Dinner cancelled")

del invite_list[1]
del invite_list[0]

if len(invite_list) == 0:
    print("\nAll woe my empty broken table")
else:
    print("\nYou screwed up the uninvite")