
# List of numbers to check if they are all greater than zero
numbers = [1, 2, 3, 4, 5]

# Using a for loop and an if statement to check each number individually
is_all_positive_individually = all(num > 0 for num in numbers)
print("All numbers are positive individually:", is_all_positive_individually)

# Directly using the all() function
is_all_positive_all = all(numbers)
print("All numbers are positive directly with all():", is_all_positive_all)

if not False:
    print("False is considered as false, so the following code does not execute")
    some_code()  # Some arbitrary code that doesn't get executed
