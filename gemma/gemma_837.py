
def function():
    try:
        print("Inside try")
        raise ValueError("An error occurred")
    finally:
        print("Inside finally")

function()

# Output:
# Inside try
# Inside finally
# Traceback (most recent call last):
#   File "my_program.py", line 4, in function
#   ValueError: An error occurred
