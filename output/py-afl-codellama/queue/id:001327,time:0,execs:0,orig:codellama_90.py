# This program demonstrates the use of "and" and "dict" in Python

# Create a dictionary with some key-value pairs
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Use "and" to check if both conditions are true
if my_dict["name"] == "Alice" and my_dict["age"] >= 21:
    print("You can vote!")
else:
    print("Sorry, you cannot vote yet.")