
# This Python program demonstrates the use of and and in operators.

# Define a list of fruits.
fruits = ["apple", "banana", "cherry", "orange", "peach"]

# Check if a fruit is in the list.
if "apple" in fruits and "cherry" in fruits:
    print("Apple and cherry are in the list.")

# Check if the list contains a fruit.
if "mango" not in fruits:
    print("Mango is not in the list.")

# Print the fruits in the list.
print("The fruits in the list are:")
for fruit in fruits:
    print(fruit)
