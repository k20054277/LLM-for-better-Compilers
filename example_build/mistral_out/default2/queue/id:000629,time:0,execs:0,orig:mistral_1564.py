
import asyncio

class MyClass:
    # Define a class variable
    _counter = 0
    
    @classmethod
    @asyncio.coroutine
    def from_counter(cls, start=0):
        """Create a new instance of the class with an optional starting counter value."""
        instance = MyClass()
        instance._counter = start
        yield from asyncio.sleep(1)  # Wait for a second before returning
        return instance
    
    @asyncio.coroutine
    def increment_counter(self):
        """Increment the counter by one."""
        self._counter += 1
        print(f"Counter is now: {self._counter}")
        yield from asyncio.sleep(0.1)

async def main():
    # Create two instances of the class, with different starting counters
    instance1 = await MyClass.from_counter()
    instance2 = await MyClass.from_counter(3)
    
    # Increment each counter five times and print the results
    for _ in range(5):
        await instance1.increment_counter()
        await instance2.increment_counter()
        
asyncio.run(main())
