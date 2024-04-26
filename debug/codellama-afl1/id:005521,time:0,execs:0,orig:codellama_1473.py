x = input("Enter a number: ")
y = input("Enter another number: ")

# Assert that x is less than or equal to y
assert x <= y, "The first number must be less than or equal to the second number."

# If x is greater than y, print an error message
if x > y:
    print("Error: The first number must be less than or equal to the second number.")