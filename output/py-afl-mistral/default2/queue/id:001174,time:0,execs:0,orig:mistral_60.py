
class MyClass:
    def __init__(self):
        self.bool_attribute = False
        self.another_false_attribute = False
        self.third_attribute = False

# Create an instance of MyClass
my_instance = MyClass()

# A dictionary to map attribute names to their values
attributes_dict = {
    'bool_attribute': True,  # Change the value for demonstration purposes
    'another_false_attribute': False,
    'third_attribute': None
}

# Use getattr() function to retrieve the attributes of an instance based on their names from the dictionary
for attribute_name, attribute_value in attributes_dict.items():
    setattr(my_instance, attribute_name, attribute_value)  # Set the attributes if needed
    print(f"The value of {attribute_name} is: {getattr(my_instance, attribute_name)}")

# Checking some false values in the instance
print("Is bool_attribute False? ", not getattr(my_instance, 'bool_attribute'))  # This will print True because the value of bool_attribute was changed to True earlier
print("Is another_false_attribute False? ", getattr(my_instance, 'another_false_attribute'))  # This will print False as it is defined in the class and not changed
