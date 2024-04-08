
# Function with a local variable
def check_numbers(a, b):
    # Initialize local variable 'is_both_positive' to False
    is_both_positive = False
    
    # Check if both numbers are positive using 'and' keyword
    if a > 0 and b > 0:
        is_both_positive = True
    
    return is_both_positive

# Global variable
x = -5
y = 3

# Function to update global variable
def increment_global():
    global x, y
    x += 1
    y += 1

# Check if numbers are positive
if check_numbers(x, y):
    print("Both numbers are positive")
else:
    print("At least one number is not positive")

# Update global variable
increment_global()
increment_global()

print("Updated values of x and y:", x, y)
