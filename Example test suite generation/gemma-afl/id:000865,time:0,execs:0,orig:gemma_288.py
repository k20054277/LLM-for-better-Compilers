
def function_with_false_and_finally():
    try:
        print("Inside try")
        raise ValueError("An error occurred")
    finally:
        print("Inside finally")

function_with_false_and_finally()

# Output:
# Inside try
# Inside finally
# Traceback (most recent call last):
#   File "<stdin>", line 4, in function_with_false_and_finally
#   ValueError: An error occurred
