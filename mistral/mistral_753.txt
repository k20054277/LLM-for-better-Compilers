
# Demonstrating the use of True
boolean_value = True
if boolean_value:
    print("This statement will be executed")
else:
    print("This statement will not be executed")

# Creating objects and demonstrating memory management
class MyClass:
    def __init__(self, value):
        self.value = value

objects = []
for i in range(100000):
    obj = MyClass(i)
    objects.append(obj)

# Manually releasing memory (not necessary in Python)
# for obj in objects:
#     del obj

# GC will free up the memory used by the objects when they are no longer needed
print("Objects created:", len(objects))
