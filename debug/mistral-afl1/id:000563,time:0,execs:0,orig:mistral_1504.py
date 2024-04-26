
# Function to check if a number is even or odd
def is_even(num):
    return num % 2 == 0

# Main function
def main():
    # Initialize a variable with an odd value
    num = 5

    # Check if the number is even using assert statement
    assert is_even(num), f"The number {num} is not even."

    # If the number was odd, we divide it by 2 and assign the result back using //= operator
    num //= 2

    print("The number is now:", num)

if __name__ == "__main__":
    main()
