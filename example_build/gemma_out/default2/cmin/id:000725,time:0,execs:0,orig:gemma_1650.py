
import asyncio

# Define a class with an async method and a staticmethod
class MyClass:
    @staticmethod
    async def my_async_method():
        print("Async method")

    @staticmethod
    def my_static_method():
        print("Static method")

# Define an asynchronous function
async def my_async_function():
    print("Async function")

# Run the async method and the static method in parallel
asyncio.gather(MyClass.my_async_method(), MyClass.my_static_method(), my_async_function())

# Output
# Async method
# Static method
# Async function
