
# Define some variables with different data types and values
numbers = [1, 5, -3, 8, 2]
number_one = 7
another_number = -1
boolean = True

# Use min() to find the smallest number in the list
smallest_number = min(numbers)
print("The smallest number in the list is:", smallest_number)

# Use a conditional statement and Boolean value
if number_one > another_number:
    print(f"{number_one} is greater than {another_number}")
else:
    print(f"{number_one} is not greater than {another_number}")
    
# Use min() to find the smallest of two numbers
smallest = min(number_one, another_number)
print("The smallest of", number_one, "and", another_number, "is:", smallest)
