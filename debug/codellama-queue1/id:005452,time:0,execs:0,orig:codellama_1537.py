import asyncio

async def get_attribute(obj, attr):
    if hasattr(obj, attr):
        return getattr(obj, attr)
    else:
        raise AttributeError(f"Object {obj} does not have attribute {attr}")

# Example usage
class MyClass:
    async def my_method(self):
        print("Hello from my method")

my_object = MyClass()

# This will print "Hello from my method"
asyncio.run(get_attribute(my_object, 'my_method')())