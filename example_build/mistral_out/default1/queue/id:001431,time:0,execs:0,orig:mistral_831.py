
# Define some variables
num = 10
is_even = num % 2 == 0
is_positive = num > 0

print("Number is even:", is_even)
print("Number is positive:", is_positive)

# Use and operator to check if number is even and positive
if is_even and is_positive:
    print(f"The number {num} is even and positive")
else:
    print(f"The number {num} is not even or not positive")

# Use chr() function to print character at index 0 of ASCII string
character = chr(65)
print("Character represented by ASCII code 65:", character)
