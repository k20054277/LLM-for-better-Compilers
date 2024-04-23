class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says 'Woof!'")

class GoldenRetriever(Dog):
    def __init__(self, name):
        super().__init__(name)
        self.breed = "Golden Retriever"
    
    async def bark(self):
        await asyncio.sleep(1)
        print(f"{self.name} says 'Arf arf!'")

dog = GoldenRetriever("Fido")
dog.bark() # Output: Fido says 'Woof!'; then after 1 second, the output: Fido says 'Arf arf!'