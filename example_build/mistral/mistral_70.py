
# Define some base and derived classes
class BaseClass:
    pass

class DerivedClass(BaseClass):
    pass

# Using False
x = 10
y = "hello"
z = False
print("x is false:", x is False)
print("y is false:", y is False)
print("z is false:", z)

# Using issubclass()
print("Is DerivedClass a BaseClass?", issubclass(DerivedClass, BaseClass))
