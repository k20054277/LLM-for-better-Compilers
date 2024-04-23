
async def my_async_function(x):
    # This function will take a long time to complete, so it is marked as asynchronous
    await asyncio.sleep(x)
    return x * 2

# Define a class with an attribute that is an asynchronous function
class MyClass:
    async def my_async_attr(self):
        return await my_async_function(5)

# Create an instance of the class and access its asynchronous attribute
my_object = MyClass()
my_result = await my_object.my_async_attr()

# Print the result
print(my_result)
