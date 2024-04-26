
# Define MyClass with an is_active boolean flag
class MyClass:
    def __init__(self):
        self.is_active = False

    # Method to toggle the flag's state
    def toggle(self):
        self.is_active = not self.is_active

# Instantiate an object of MyClass
my_instance = MyClass()

# Demonstrating the use of False and OOP by checking and toggling the flag
if my_instance.is_active is False:
    print("The flag is currently set to False.")
else:
    print("The flag is currently set to True.")

my_instance.toggle()  # Toggle the flag's state
print(f"The new flag status is: {my_instance.is_active}")
