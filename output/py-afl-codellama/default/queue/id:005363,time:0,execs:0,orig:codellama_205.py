# Demonstrate the use of False and eval

# Define a function that takes a string argument
def test(s):
    # Use eval to evaluate the string as a boolean expression
    result = eval(s)
    print("The result of evaluating '%s' is %s" % (s, result))

# Test the function with some examples
test('True')  # Output: The result of evaluating 'True' is True
test('False')  # Output: The result of evaluating 'False' is False
test('1 == 2')  # Output: The result of evaluating '1 == 2' is False
test('1 != 2')  # Output: The result of evaluating '1 != 2' is True