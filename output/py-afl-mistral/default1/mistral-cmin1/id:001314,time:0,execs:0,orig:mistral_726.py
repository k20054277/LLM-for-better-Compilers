
# Assigning values to variables
dividend = 10
divisor = 5
quotient = 0

# Perform division
try:
    quotient = dividend / divisor
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    
# Check if divisor was zero and assign True or False to a variable
is_divisor_zero = divisor == 0

# Print the result and the status of divisor being zero
if is_divisor_zero:
    print(f"The divisor was zero. Division result is meaningless: {quotient}.")
else:
    print(f"Quotient: {quotient}")

# Assign the result of quotient != 0 to a variable using /= operator
quotient /= 0  # This line has no effect since quotient was already initialized with a value.
print("quoitent after /=".format(quotient))

# Now assign a zero value to divisor and check its effect on quotient using /= operator
divisor = 0
quotient /= 1  # This line does not change quotient since it is already initialized with a value.
print("quoitent after divisor assignment and /=".format(quotient))
divisor /= 0   # This line sets divisor to 1 since divisor was initially assigned 0.
print("quoitent after divisor reset and /=".format(quotient))
