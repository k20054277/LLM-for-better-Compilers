
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_student = True

    def greet(self):
        print(f"Hello, {self.name}!")

my_obj = MyClass("John Doe", 25)

# Check if is_student is False for my_obj
if not my_obj.is_student:
    print("This object is not a student.")
else:
    print("This object is a student.")

# Print all the attributes and methods of my_obj using dir()
print(dir(my_obj))
