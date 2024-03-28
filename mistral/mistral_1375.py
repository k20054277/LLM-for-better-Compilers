
# Define a function with expected arguments
def calculate_sum(num1, num2):
    total = num1 + num2
    assert type(num1) is int and type(num2) is int, "Both num1 and num2 must be integers."
    return total

# Define some variables with incorrect types
try:
    a = 5
    b = '3'
    c = calculate_sum(a, b)
except AssertionError as error_msg:
    print(error_msg)

print("\nVariables and their values within the current scope:")
for name, value in vars().items():
    print(f"{name}: {value}")

# Define variables with correct types
num1 = 3
num2 = 4
result = calculate_sum(num1, num2)
print(f"\nSum of {num1} and {num2}: {result}")
