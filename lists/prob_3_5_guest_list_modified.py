invite_list = ['Alexander', 'Genghis Khan', 'Lee Kuan Yew']

for person in invite_list:
    print(f'Welcome to my dinner {person}')

print(f"\nLooks like {invite_list.pop(1)} can't make it to dinner. Need to invite more people now")

for person in invite_list:
    print(f'\nPerson in list: {person}')

invite_list.append("Teddy Roosevelt")
invite_list.append("Nicola Tesla")
print()

for person in invite_list:
    print(f'Welcome to my dinner {person}')