
class MyClass:
    def __init__(self, value):
        self.value = value

def function(arg=None):
    if arg is None:
        print("Argument is None.")
    else:
        print("Argument is not None and its type is:", type(arg))
        my_instance = MyClass(arg)
        print("Instance of MyClass created with argument:", my_instance.value)

# Testing the function with different arguments, including None
function()
function(5)
function("hello")
function(MyClass(42))
