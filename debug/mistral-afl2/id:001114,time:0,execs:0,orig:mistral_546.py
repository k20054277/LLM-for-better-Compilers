
import sys

class MyClass:
    def __init__(self, attr1=True, attr2='default'):
        self.attr1 = attr1
        self.attr2 = attr2

    def print_attributes(self):
        print(f'Attr1: {self.attr1}')
        print(f'Attr2: {self.attr2}')

# Instantiate the class and print initial attributes
my_instance = MyClass()
my_instance.print_attributes()

# Demonstrating the usage of True
another_instance = MyClass(False)
another_instance.print_attributes()

# Now let's delete an attribute (attr1) from 'my_instance' using delattr()
sys.modules.builtins.delattr(my_instance, 'attr1')

# Print the modified attributes of 'my_instance'
my_instance.print_attributes()
