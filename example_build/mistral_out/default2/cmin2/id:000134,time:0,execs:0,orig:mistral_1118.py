
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using reversed() function to get a reverse iterator
reverse_iterator = reversed(numbers)

# Iterating through the reversed iterator using for loop and as keyword
print("Iterating through reversed iterator:")
for num in reversed(numbers):
    print(num)

print("\nUsing as keyword to assign reversed iterator to a variable:")
# Assigning reversed iterator to a variable using as keyword
my_reverse_iterator = reversed(numbers)

# Iterating through the assigned reversed iterator using for loop
for num in my_reverse_iterator:
    print(num)
