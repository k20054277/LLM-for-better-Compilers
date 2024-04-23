
# This Python program demonstrates the use of assert and eval

# Define a function to evaluate an expression
def evaluate_expression(expression):
    # Use eval to evaluate the expression
    result = eval(expression)
    # Assert that the result is equal to 10
    assert result == 10

# Examples of expressions to evaluate
expression1 = "5 + 5"
expression2 = "10 - 2"

# Evaluate the expressions
evaluate_expression(expression1)
evaluate_expression(expression2)

# Print the results
print("Expression 1:", expression1, "->", evaluate_expression(expression1))
print("Expression 2:", expression2, "->", evaluate_expression(expression2))
