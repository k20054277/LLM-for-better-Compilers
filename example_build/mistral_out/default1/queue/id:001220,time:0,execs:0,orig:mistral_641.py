
# Define a list of boolean values
boolean_list = [True, False, True, False, True]

# Print the original list
print("Original List:")
print(boolean_list)

# Using a for loop to iterate through each boolean value and print it along with its index
print("\nIterating through the list and printing each boolean value:")
for index, value in enumerate(boolean_list):
    print(f"Index: {index}, Value: {value}")

# Using a list comprehension to create a new list that contains only the True values
true_values = [value for value in boolean_list if value is True]

# Print the new list of True values
print("\nList of True values:")
print(true_values)

# Using the sum() function to count the number of True values in the original list
num_of_trues = sum(boolean_list)

# Print the number of True values in the original list
print(f"\nNumber of True values in the Original List: {num_of_trues}")
