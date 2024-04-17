
# List of numbers to be sorted
numbers = [5, 2, 8, 1, 6, 3]

# Using the 'and' keyword for condition checks
even_numbers = []
for number in numbers:
    if number % 2 == 0 and number > 1:
        even_numbers.append(number)

print("Even numbers greater than 1 are:", even_numbers)

# Using the 'sorted' keyword to sort a list
sorted_numbers = sorted(numbers)
print("Sorted list of numbers is:", sorted_numbers)
