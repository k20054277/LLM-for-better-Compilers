
def function_with_try_and_finally():
    try:
        print("Inside try")
        raise ValueError("This is an error")
    finally:
        print("Inside finally")

function_with_try_and_finally()
