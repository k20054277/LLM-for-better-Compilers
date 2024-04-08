
# Define a custom class named MyClass
class MyClass:
    # Define some custom attributes
    def __init__(self, value=0):
        self.my_true = True
        self.my_false = False
        self.my_value = value

# Create an instance of the class
my_instance = MyClass(42)

# Accessing attributes using dot notation
print("Accessing attributes using dot notation:")
print(f"True value: {my_instance.my_true}")
print(f"False value: {my_instance.my_false}")
print(f"Value: {my_instance.my_value}")

# Accessing attributes using getattr()
print("Accessing attributes using getattr():")
for attr in ['my_true', 'my_false', 'my_value']:
    print(f"{attr}: {getattr(my_instance, attr)}")
