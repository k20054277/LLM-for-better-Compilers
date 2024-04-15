
# Define a simple list
my_list = [1, 2, 3, 4, 5]

# Iterate through the list and use assert statements to check each element
for i in my_list:
    # Expected value for each element (in this case, the index + 1)
    expected = i + 1
    
    # Use an assert statement to check if the actual value equals the expected value
    assert i == expected, f"Element at position {my_list.index(i)} is not equal to the expected value: {expected}"

# If we reach this point in the code, all assertions have passed
print("All assertions have passed!")
