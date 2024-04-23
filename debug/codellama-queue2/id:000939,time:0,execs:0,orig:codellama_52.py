class Dog:
    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")
dog2 = Dog("Max")

if dog1 == dog2:
    print("Dogs are the same")
else:
    print("Dogs are not the same")