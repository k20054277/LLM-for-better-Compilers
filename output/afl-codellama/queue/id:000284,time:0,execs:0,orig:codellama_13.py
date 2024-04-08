# This is an example of using a context manager with a "with" statement in Python

class MyContextManager:
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        print("Entering the context")
        return self.value

    def __exit__(self, type, value, traceback):
        if type is not None:
            print(f"Exception occurred: {type}")
        else:
            print("Exiting the context")

with MyContextManager(5) as x:
    print(x)  # This will print "5"