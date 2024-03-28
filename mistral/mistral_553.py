
# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use a lambda function with filter to keep only numbers greater than 5
filtered_numbers = filter(lambda x: x > 5, numbers)

# Convert the filter object to a list and assign it to a variable
filtered_numbers_list = list(filtered_numbers)

print("Numbers greater than 5:")
for num in filtered_numbers_list:
    print(num)

print("\nUsing True instead of lambda function:")
# Use filter with the constant True value to keep all elements
filtered_numbers_using_true = filter(True, numbers)

# Convert the filter object to a list and assign it to a variable
filtered_numbers_using_true_list = list(filtered_numbers_using_true)

print("All numbers:")
for num in numbers:
    print(num)

print("\nNumbers that remain after filtering with True:")
for num in filtered_numbers_using_true_list:
    print(num)
