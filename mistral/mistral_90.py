
# Define a decimal number with more digits than needed
decimal_number = 3.14159265358979323846

# Check if the number 0 is equal to the decimal number (-0 and 0 are considered equal in Python)
if 0.0 == decimal_number:
    print("Decental number is equal to zero (False due to type checking)")
else:
    # Round the decimal number to two decimal places using round function
    rounded_number = round(decimal_number, 2)
    print(f"Rounded decimal number to two decimal places: {rounded_number}")

# Use False as a boolean value in if statement
if not (decimal_number > 3):
    print("Decental number is less or equal than 3")
else:
    print("Decental number is greater than 3")