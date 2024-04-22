
# This is a simple Python program that demonstrates the usage of None and enumerate()

# List of fruits with some elements being None
fruits = ["apple", "banana", None, "orange", None]

def print_fruit_and_index(item):
    # The enumerate function returns a tuple for each item in the iterable,
    # containing an index and that item. We assign these to variables 'i' and 'f' respectively
    i, f = enumerate(fruits)
    
    if f is not None:
        print("Fruit:", f)
        print("Index:", i)
        print()

print("Fruits with their indices:")
print_fruit_and_index(None)  # Calling the function with None as argument
print_fruit_and_index("grape")
