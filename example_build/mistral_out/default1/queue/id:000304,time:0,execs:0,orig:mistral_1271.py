
# Define a tuple with two tuples as elements
complex_data = (1, 2, ('a', 'b'), (3, 4))

# Use unpacking and assignment with 'as' to separate the first two elements of the complex data
x, rest = complex_data[0:2]
print(f"First two elements: {x}, {rest}")

# Check if a specific value is present in the tuple using 'in'
if 'a' in complex_data:
    print("The tuple contains 'a'")
else:
    print("The tuple does not contain 'a'")
