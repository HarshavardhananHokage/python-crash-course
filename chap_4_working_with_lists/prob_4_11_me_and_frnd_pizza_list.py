my_pizza_list = ["Margerita", "Quattro Formaggi", "Prosciutto"]

my_frnd_pizza_list = my_pizza_list[:]


print(my_pizza_list)
print(my_frnd_pizza_list)

print("\nadding Capricciosa to my list and Diavola to my friends...")

my_frnd_pizza_list.append("Diavola")
my_pizza_list.append("Capricciosa")


print("\nUpdated list\nMy List")
print(my_pizza_list)
print("\nMy friend List")
print(my_frnd_pizza_list)