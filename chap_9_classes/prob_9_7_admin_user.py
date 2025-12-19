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
        print(greeting)

class Admin(User):
    def __init__(self, first_name, last_name, age, privileges=None):
        super().__init__(first_name, last_name, age, "Administration")
        self.privileges = list(privileges) if privileges is not None else []

    def show_privileges(self):
        print(self.privileges)

if __name__ == "__main__":
    administrator_kentucky = Admin("Harland", "Sanders", 100, ["can order",
                                                          "can close shop", "can pay bills", "can hire people", "can sleep in car"])

    administrator_kentucky.show_privileges()
    administrator_kentucky.describe_user()
    administrator_kentucky.greet_user()