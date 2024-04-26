
def my_function(x, y):
    """
    This function checks if two numbers are equal and greater than 10.
    """
    if x > 10 and y > 10:
        print("Both x and y are greater than 10.")
        result = x + y
    else:
        print("Either x or y is not greater than 10.")
        result = None

    # Use locals() to print all local variables in the current scope.
    print("Local variables:")
    for key, value in locals().items():
        if key != "self":
            print(f"{key}: {value}")

    return result

if __name__ == "__main__":
    my_function(15, 20)
