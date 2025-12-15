class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restuaurant is {self.restaurant_name} and it serves {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print("Restaurant open for business!!!")

class IceCreamStand(Restaurant):
    def __init__(self, stand_name, flavors=None):
        super().__init__(stand_name, "Ice Cream")
        self.flavors = flavors if flavors else ["vanilla"]

    def add_new_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Flavour {flavor} already present")
        else:
            self.flavors.append(flavor)

    def print_flavors_served(self):
        print(f"Flavors Served: {self.flavors}")

abraham_lincoln_ice_cream_stand = IceCreamStand("Abraham Lincoln Ice Cream Stand", ["vanilla", "strawberry", "chocolate"])
abraham_lincoln_ice_cream_stand.add_new_flavor("mango")
abraham_lincoln_ice_cream_stand.add_new_flavor("strawberry")
abraham_lincoln_ice_cream_stand.add_new_flavor("spicy sriracha 4X")

abraham_lincoln_ice_cream_stand.describe_restaurant()
abraham_lincoln_ice_cream_stand.open_restaurant()
abraham_lincoln_ice_cream_stand.print_flavors_served()