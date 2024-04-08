
# Define two variables
num1 = 10
num2 = 3

# Use the and operator to check if num1 is greater than 5 and num2 is even
if num1 > 5 and num2 % 2 == 0:
    print(f"{num1} is greater than 5 and {num2} is even")
else:
    print("Either num1 is less than or equal to 5 or num2 is odd")

# Use the divmod() function to find quotient and remainder of division of num1 by num2
quotient, remainder = divmod(num1, num2)

print(f"The quotient of {num1} divided by {num2} is {quotient} and the remainder is {remainder}")
