
# Initialize some variables
num1 = 10
num2 = 4
quota_remainder = True

# Perform floor division and assign the quotient and remainder to num1 and num2 respectively
num1, num2 = divmod(num1, num2)

# Check if there is any remainder
if num2 != 0:
    quota_remainder = False

# Demonstrate the use of floor division assignment (//=) on num1
num1 //= 2

print("Quotient: {}".format(num1))
print("Remainder: {}".format(num2))
print("Quota remainder: {}".format(quota_remainder))
