
class MyClass:
    def __init__(self, value):
        assert value >= 0, "Value should be non-negative"
        self._private = value

    def remove_attribute(self, attribute_name):
        delattr(self, attribute_name)
        print(f"Successfully removed the attribute {attribute_name}.")

# Instantiate an object of MyClass with a valid value
my_instance = MyClass(5)
print("My instance attributes: ", dir(my_instance))

# Instantiate an object of MyClass with an invalid value (should raise an AssertionError)
try:
    invalid_instance = MyClass(-3)
except AssertionError as e:
    print(e)

# Remove a non-existent attribute (should not raise any error)
my_instance.remove_attribute("non_existent_attribute")
print("My instance attributes after removal: ", dir(my_instance))

# Remove an existing attribute (private _private)
my_instance.remove_attribute("_private")
print("My instance attributes after removing '_private': ", dir(my_instance))
