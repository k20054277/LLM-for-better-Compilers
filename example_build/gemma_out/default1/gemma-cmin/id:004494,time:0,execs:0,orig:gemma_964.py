
# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use the and operator to check if the number is greater than 5 and less than 10
for num in numbers:
    if num > 5 and num < 10:
        print(num)

# Output:
# 6
# 7
# 8

# Create a dictionary to store key-value pairs
employees = {"John Doe": 100000, "Jane Doe": 200000, "Peter Pan": 300000}

# Use the and operator to check if the key is "John Doe" and the value is 100000
for key, value in employees.items():
    if key == "John Doe" and value == 100000:
        print(key, value)

# Output:
# John Doe 100000
