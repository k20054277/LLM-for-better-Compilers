
# Demonstrating True and enumerate

# Define a list of fruits
fruits = ["apple", "banana", "orange", "mango"]

# Use True to check if the list is empty
if not fruits:
    print("The list is empty")

# Use enumerate to get the index and item of each element in the list
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# Print the fruits using True and enumerate
print("Fruits:")
for fruit in fruits:
    if fruit is True:
        print(fruit)
