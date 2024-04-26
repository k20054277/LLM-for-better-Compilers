
# List of input tuples
input_list = [(1, 2), (3, 4), (5, 6)]

# Function to be applied on each tuple
def square_map(x):
    return x[0] ** 2

# Using map and as keyword (Python doesn't support)
# output = list(map(lambda x: x[0]**2, input_list))

# Using List Comprehension with generator expression instead of map
output = [x[0]**2 for x in input_list]

print("Using Map and as keyword (Python doesn't support):")
# Uncomment the above comment to test it
# print(output)

print("\nUsing List Comprehension with generator expression:")
print(output)
