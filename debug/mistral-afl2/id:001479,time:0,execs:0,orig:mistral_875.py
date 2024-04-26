
# Define a list of integers
numbers = [1, 2, 3, 4, 5]

# Use and operator to check if an element is even and greater than 3
print("Numbers in the list that are even and greater than 3:")
for num in numbers:
    if num > 3 and num % 2 == 0:
        print(num)

# Use reversed function to iterate through a list in reverse order
print("\nElements in the list 'numbers' in reverse order:")
for num in reversed(numbers):
    print(num)
