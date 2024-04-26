def greet(name):
    print("Hello, " + name)

greet("Alice")
greet("Bob")

if True and False:
    print("This will not be printed.")
else:
    print("This will be printed.")

if greet("Alice") and greet("Bob"):
    print("Both greets were successful.")