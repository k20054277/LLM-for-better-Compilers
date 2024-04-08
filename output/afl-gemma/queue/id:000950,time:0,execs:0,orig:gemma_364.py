
# This Python program demonstrates the use of False and slice

# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print the numbers in the list
print(numbers)

# Print the numbers in the list that are divisible by 2
print(numbers[::2])

# Print the numbers in the list that are greater than 5
print(numbers[numbers > 5])

# Print the numbers in the list that are less than 5
print(numbers[numbers < 5])

# Print the numbers in the list that are equal to 5
print(numbers[numbers == 5])

# Print the numbers in the list that are not equal to 5
print(numbers[numbers != 5])

# Print True or False based on whether the number 5 is in the list
print(5 in numbers)

# Print True or False based on whether the number 11 is in the list
print(11 in numbers)

# Print True or False based on whether the list is empty
print(not numbers)
