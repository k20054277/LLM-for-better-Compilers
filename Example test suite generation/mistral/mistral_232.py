
# Using regular multiplication
def multiply(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Base number and exponent to be raised
number = 2
power = 3

print(f"Number: {number}")
print(f"Exponent: {power}")
print(f"Number raised to the power using regular multiplication: {multiply(number, power)}")

# Using compound power assignment
def raise_to_power(base, power):
    base **= power

# Base number and exponent to be raised
number = 2
power = 3

print(f"Base number: {number}")
print(f"Exponent: {power}")
raise_to_power(number, power)
print(f"Number raised to the power using compound power assignment: {number}")
