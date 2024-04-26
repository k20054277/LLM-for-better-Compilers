
def calculate_square_root(number):
    """Calculate the square root of a given number"""
    assert number >= 0, "Error: Number must be non-negative"
    return number ** 0.5

# Using assert statement
def main():
    try:
        num = int(input("Enter a number: "))
        result = calculate_square_root(num)
        print(f"Square root of {num} is {result}")
    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    main()
