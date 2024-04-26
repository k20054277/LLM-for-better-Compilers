
# This variable x is assigned a value of None
x = None

# We can also assign None directly to functions or method return types
def my_function():
    return None

# Or in classes as default values for methods
class MyClass:
    def my_method(self):
        pass
        return None

# Now let's print some messages using print()
print("The value of variable x is:", x)
print("My function returns:", my_function())
instance = MyClass()
print("The default method of instance returns:", instance.my_method())
