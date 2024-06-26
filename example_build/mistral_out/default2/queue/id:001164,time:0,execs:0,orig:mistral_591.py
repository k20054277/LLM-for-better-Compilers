
# List of some numbers and strings
data = [3, 5, 1, 2, 7, 4, "apple", "banana", "orange"]

# Using True in a conditional statement
if True:
    print("This block will always be executed.")

# Sorting the data list using sorted() function
sorted_data = sorted(data)
print("Sorted data:")
print(sorted_data)

# Sorting data in place (modifying the original list) by setting the keyword argument 'inplace' to True
data.sort(key=lambda x: abs(x), reverse=True, inplace=True)
print("Sorted data in place:")
print(data)
