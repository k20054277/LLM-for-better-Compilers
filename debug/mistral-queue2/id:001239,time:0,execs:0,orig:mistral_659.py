
# Define some variables
num1 = 10
num2 = 20
is_even = num1 % 2 == 0

print("Num1 is even?: ", is_even)

# Using True in if statements
if True:
    print("This block will always execute")

# Boolean expressions
print("Num1 is greater than Num2: ", (num1 > num2))
print("Absolut value of Num1 is greater than 10 and Num2 is less than 5: ", ((abs(num1) > 10) and (num2 < 5)))
print("Num1 is even or Num2 is odd: ", ((num1 % 2 == 0) or (num2 % 2 != 0)))
