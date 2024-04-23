
# Demonstration of as and in

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Iterate over the list and print each number
for num in numbers:
    print(num)

# Use as to bind the iterator to a variable
iterator = iter(numbers)

# Iterate over the iterator and print each number
for num in iterator:
    print(num)

# Print the elements of the list using as and in
print(f"The elements of the list are: {', '.join(str(num) for num in numbers)}")

# Print the elements of the iterator using as and in
print(f"The elements of the iterator are: {', '.join(str(num) for num in iterator)}")
