
# Define a calculator namespace
calculator = {
    'add': lambda x, y: x + y,
    'multiply': lambda x, y: x * y
}

# Use the calculator functions and assert their results
def test_calculator():
    result_add = calculator['add'](3, 4)
    result_multiply = calculator['multiply'](3, 4)

    # Assert addition is correct
    assert result_add == 7, f"Addition is not correct. Expected: 7, Got: {result_add}"

    # Assert multiplication is correct
    assert result_multiply == 12, f"Multiplication is not correct. Expected: 12, Got: {result_multiply}"

if __name__ == "__main__":
    test_calculator()
