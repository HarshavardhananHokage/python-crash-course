toppings = ""

print(f"Lets make a pizza with your own toppings.\nEnter your pizza toppings below.\nType 'quit' to stop.")

while toppings != 'quit':
    toppings = input("Enter toppings: ")
    if(toppings == 'quit'):
        break;
    print(f"Adding {toppings} to pizza....")

print(f"Annanukku suda suda oru custom pizza parcel!!!!")