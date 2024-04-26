class MyClass:
    def __init__(self):
        self.x = 5
        self.y = 10
    
    def my_method(self):
        print("Inside my_method")

obj = MyClass()

# Use and to check if both x and y are greater than 0
if obj.x > 0 and obj.y > 0:
    print("Both x and y are greater than 0")

# Use getattr to call the my_method method on obj
getattr(obj, "my_method")()