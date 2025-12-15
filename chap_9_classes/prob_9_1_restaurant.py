class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restuaurant is {self.restaurant_name} and it serves {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print("Restaurant open for business!!!")

ganesh_bhavan = Restaurant("Ganesh Bhavan", "South Indian")
ganesh_bhavan.describe_restaurant()
ganesh_bhavan.open_restaurant()