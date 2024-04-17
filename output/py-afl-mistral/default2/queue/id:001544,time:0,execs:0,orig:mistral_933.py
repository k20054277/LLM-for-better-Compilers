
# Base Class: Animal
class Animal:
    def __init__(self, name):
        self.name = name

    # Abstract method without implementation
    def can_fly(self):
        pass

# Derived Class: Dog
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def can_jump(self):
        print(f"{self.name} can jump {self.jump_height()} cm high.")
        return self.is_young() and self.can_fetch()

    def jump_height(self):
        return 10

# Derived Class: Cat
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def can_jump(self):
        print(f"{self.name} can jump {self.jump_height()} cm high.")
        return self.is_playful() and self.can_climb_trees()

    def jump_height(self):
        return 5

# Main program
if __name__ == "__main__":
    dog = Dog("Fido", "Labrador")
    cat = Cat("Mittens", "Gray")
    
    print(f"Can {dog.name} perform well? {dog.can_jump()}")
    print(f"Can {cat.name} perform well? {cat.can_jump()}")

# Helper methods for Dog
class Dog:
    # Method 1: is_young
    def is_young(self):
        return self.age < 3

    # Method 2: can_fetch
    def can_fetch(self):
        print(f"{self.name} can fetch sticks.")
        return True
