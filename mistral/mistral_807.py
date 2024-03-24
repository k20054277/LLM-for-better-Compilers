
# Define two variables with boolean values
num1 = 10
num2 = 20
is_even_num1 = num1 % 2 == 0
is_even_num2 = num2 % 2 == 0

# Use 'and' to check if both conditions are true
if (is_even_num1 and num1 < 20) or (is_even_num2 and num2 > 30):
    print("One of the numbers is even and within certain range")
else:
    print("Neither number is even or not in the given range")
