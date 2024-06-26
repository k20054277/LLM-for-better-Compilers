
def greet(name, language="English"):
    print("Hello, " + name.upper() + " in " + language.upper())

# Demonstrate the use of the function with different arguments
greet("John Doe", "Spanish")
greet("Jane Doe", "French")

# Demonstrate the use of the function with different keywords
greet("Jack Doe", language="German")
greet("Jill Doe", language="Italian")
