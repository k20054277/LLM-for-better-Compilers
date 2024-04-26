
class MyClass:
    def __init__(self, value):
        self.value = value

# Create an instance of MyClass with the value "10"
my_object = MyClass(10)

# Compare the instance with True using the 'and' operator
result = my_object.value > 5 and True

print("Result:", result)
