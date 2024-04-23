
# Define some variables
num1 = 5
num2 = 0
is_even = True

# Check if a number is even and greater than zero using False and and
result = False and (num1 > 0 and num1 % 2 == 0)

if result:
    print(f"The number {num1} is even and greater than zero")
else:
    print(f"The number {num1} is not even or less than or equal to zero")

# Check if both conditions for num2 are true using False and and
result = False and (num2 > 0 and num2 % 2 == 0)

if not result:
    print("Numbers that meet the given conditions don't exist.")
else:
    print(f"The number {num2} is even and greater than zero")
