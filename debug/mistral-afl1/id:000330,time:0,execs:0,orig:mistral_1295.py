
# Define a function with expected preconditions using assert statement
def divide(x, y):
    assert y != 0, "Error: Division by zero is not allowed."
    result = x / y
    return result

# Function to get user input for number and denominator
def get_input():
    num = int(input("Enter the numerator: "))
    den = int(input("Enter the denominator: "))
    return num, den

# Main program flow
if __name__ == "__main__":
    num, den = get_input()
    try:
        result = divide(num, den)
        print(f"Result: {result}")
    except AssertionError as e:
        print("Error:", e)
