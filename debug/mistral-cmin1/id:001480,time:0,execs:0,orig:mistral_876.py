
# Define variables
num1 = 5.6234
num2 = 2
limit = 3

# Check if condition is true using and keyword
if num1 > 5 and num2 < 3:
    print("Condition 1 is true")
else:
    print("Condition 1 is false")

# Round a number using round() function
result = round(num1, 2)
print(f"Rounded value of num1 to 2 decimal places: {result}")

# Check if condition is true with rounding using and keyword
if round(num1, 2) > limit and num2 < 3:
    print("Condition 2 is true")
else:
    print("Condition 2 is false")
