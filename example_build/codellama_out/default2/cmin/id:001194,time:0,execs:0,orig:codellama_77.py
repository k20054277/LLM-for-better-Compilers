numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = []

# Use any to check if any number in the list is less than 5
if any(number < 5 for number in numbers):
    # If any number is less than 5, add it to the filtered_numbers list
    filtered_numbers.extend(number for number in numbers if number < 5)

# Use and to check if all numbers in the list are even
if all(number % 2 == 0 for number in numbers):
    # If all numbers are even, add them to the filtered_numbers list
    filtered_numbers.extend(number for number in numbers if number % 2 == 0)

print(filtered_numbers)