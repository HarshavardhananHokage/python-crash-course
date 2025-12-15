class User:
    def __init__(self, first_name, last_name, age, dept="no", is_active=True):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.dept = dept
        self.is_active = is_active

    def describe_user(self):
        description = (f"User's name is {self.first_name} {self.last_name}. They are of age {self.age}. "
                      f"They belong to {self.dept} department and is an {"active" if self.is_active else "inactive"} user")
        print(description)

    def greet_user(self):
        greeting = f"Welcome {self.first_name} {self.last_name}. Have a great day!"

john_rambo = User("John", "Rambo", 50, "Jungle Massacre", is_active=False)
arnold = User("Arnold", "Schwarzenegger", 50, "Pump Iron Make Muscles", True)
jackie_chan = User("Jackie", "Chan", 50, "Parkour and Rubber Body", False)
mohammed_ali = User("Mohammed", "Ali", 50, "Sting Like a Bee, Float Like a Butterfly", True)
keanu_reeves = User("Keanu", "Reeves", 50, "Falling Down Stairs and Buildings Unscathed", True)
department_less_guy = User("Department-Less-Guy", "Just Retire Already!", 60, is_active=True)

john_rambo.describe_user()
arnold.describe_user()
jackie_chan.describe_user()
mohammed_ali.describe_user()
keanu_reeves.describe_user()
department_less_guy.describe_user()
