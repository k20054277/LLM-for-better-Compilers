
# Set two variables with numbers
num1 = 10
num2 = 5

# Use the greater than (>) operator to compare num1 and num2
is_greater = num1 > num2

# Print the result using string formatting
print("{} is greater than {}?: {}".format(num1, num2, is_greater))

# Use True directly in a statement
if num1 > num2:
    print("{0} is greater than {1}.".format(num1, num2))
else:
    print("{0} is not greater than {1}.".format(num1, num2))
