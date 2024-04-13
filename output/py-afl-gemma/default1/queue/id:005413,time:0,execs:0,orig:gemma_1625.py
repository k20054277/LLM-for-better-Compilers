
import asyncio

class Parent:
    def __init__(self, name):
        self.name = name

    async def say_hello(self):
        print("Hello, ", self.name)

class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

    async def say_hello(self):
        print("Hello, ", self.name)

        # This is an asynchronous function
        await asyncio.sleep(1)

        print("World!")

# Define an asynchronous function
async def main():
    # Create an instance of the Child class
    child = Child("John")

    # Call the say_hello method asynchronously
    await child.say_hello()

    # Print a message after the child has said hello
    print("Parent: Hello, ", child.name)

# Run the main function asynchronously
asyncio.run(main())
