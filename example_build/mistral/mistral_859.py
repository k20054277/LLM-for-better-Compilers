
# Define a list
numbers = [1, 2, 3, 4, 5]

# Set a condition with 'and'
condition = (len(numbers) > 0) and (numbers[0] > 3)

if condition:
    print("The first number is greater than 3 and the list has elements.")
else:
    print("Either the list is empty or the first number is less than or equal to 3.")

# Checking another condition with 'and' using two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
condition = (len(list1) > 0) and (len(list2) > 0)

if condition:
    print("Both lists have elements.")
else:
    print("At least one of the lists is empty.")
