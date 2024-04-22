
# Create a list of False values
false_list = [False] * 5
print("Original list of False values: ", false_list)

# Define a function that negates a boolean value
def negate(value):
    return not value

# Use map to apply the negate function to each element in false_list
negative_list = list(map(negate, false_list))
print("List of negated False values: ", negative_list)
