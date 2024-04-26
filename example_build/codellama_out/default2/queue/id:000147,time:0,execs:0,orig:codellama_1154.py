def greet(name):
    print(f"Hello, {name}!")

greet_alias = greet

# Calling the original function
greet("Alice")

# Calling the aliased function
greet_alias("Bob")