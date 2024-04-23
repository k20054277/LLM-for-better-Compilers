
# Using pow function
def raise_to_power(base, exponent):
    result = pow(base, exponent)
    return result

# Base and exponent for demonstration
base = 2
exponent = 3

raised_to_power = raise_to_power(base, exponent)
print(f"{base} raised to the power {exponent} is: {raised_to_power}")

# Using as keyword for variable renaming during function returns
def square_root(number):
    result = number ** 0.5
    return result.as_name('square_root')

number = 16
square_root_value = square_root(number)
print(f"The square root of {number} is: {square_root_value}")
