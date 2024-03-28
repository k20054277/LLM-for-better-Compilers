
# Function to check if a number is positive
def check_positive(number):
    assert number > 0, "Error: Number must be positive"
    return number

# Test the function with some values
num1 = 5
num2 = -3
num3 = 0

print("Number 1:", check_positive(num1))
print("Number 2:", check_positive(num2))
try:
    check_positive(num3)
except AssertionError as e:
    print("Error:", e)
