
# Function to apply bitwise NOT operation on a given number and return original number and result
def not_operator(num):
    result = ~num  # Bitwise NOT operation
    print(f'Original Number: {num}')
    print(f'Result (Bitwise NOT): {result}\n')
    return num, result

# Test cases for the function
if __name__ == "__main__":
    # Test case 1: Positive number
    test_num_1 = 5
    original_num, result = not_operator(test_num_1)

    # Test case 2: Negative number
    test_num_2 = -3
    original_num, result = not_operator(test_num_2)

    # Test case 3: None type
    test_num_3 = None
    print(f"Test case for None: {test_num_3}")
    if test_num_3 is not None:
        original_num, result = not_operator(test_num_3)
        print(f'Result (for None): {result}')
