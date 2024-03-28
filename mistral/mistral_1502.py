
def double(num):
    """
    This function takes an integer as an argument and returns its double value.
    """
    return num * 2

# Testing the double function using assert statement
def main():
    num = 5
    expected_result = 10
    result = double(num)

    # Using assert statement to test if the function returns the correct value
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

    print("Function tested successfully")

# Using *= operator for assignment
def increase_by_two(num):
    """
    This function takes an integer as an argument and increases its value by 2 using *= operator.
    """
    num *= 2
    return num

if __name__ == "__main__":
    main()
    num = 3
    print("Number before increasing: ", num)
    num_doubled = increase_by_two(num)
    print("Number after increasing by two: ", num_doubled)
