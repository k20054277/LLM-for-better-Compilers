
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of MyClass
my_instance = MyClass("John Doe", 30)

print(f"Name: {my_instance.name}")
print(f"Age: {my_instance.age}")

# Set some additional attributes using False (as a sentinel value)
my_instance.__dict__["is_student"] = False
my_instance.__dict__["is_employed"] = False

print(f"Is Student: {my_instance.is_student}")
print(f"Is Employed: {my_instance.is_employed}")

# Delete attributes using delattr
delattr(my_instance, "is_student")
delattr(my_instance, "is_employed")

print("After deleting attributes:")
for key in my_instance.__dict__.keys():
    print(f"{key}: {my_instance.__dict__[key]}")
