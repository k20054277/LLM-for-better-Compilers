
# Define a function to calculate the product
def calculate_product(num1, num2, multiplier=None):
    # Initialize product to 1
    product = 1
    
    if multiplier is not None:
        product *= multiplier
    
    product *= num1 * num2
    
    return product

# Take user input and assign it to variables
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
multiplier = None  # Initialize multiplier as None

# Ask user if they want to use a multiplier
answer = "yes"
while answer in ["yes", "y"]:
    multiplier = float(input("Do you want to use a multiplier? If yes, enter it: "))
    answer = input("Do you want to calculate another product? If yes, enter 'yes' or 'y': ")

# Calculate the product with or without multiplier
result = calculate_product(num1, num2, multiplier)
print(f"The product of {num1} and {num2}, multiplied by {multiplier if multiplier else ''}, is: {result}")
