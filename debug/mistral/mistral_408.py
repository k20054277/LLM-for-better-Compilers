
# Define a function that takes two arguments, returns the greater number or sets to None if both are equal
def max_number(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2
        
# Assign values to variables with some being set to None
num1 = 5
num2 = None

# Use conditional statement and check if 'num2' is None, if yes then assign default value of zero
if num2 is None:
    num2 = 0

# Get maximum number using the defined function
max_num = max_number(num1, num2)

print("Maximum number: ", max_num)
