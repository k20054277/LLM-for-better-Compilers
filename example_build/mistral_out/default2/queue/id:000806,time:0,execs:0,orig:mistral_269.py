
# A function that returns None as default value
def function_returns_none():
    print("Function that returns None")
    return None

# A global variable with an initial value
x = 0

def increment():
    # Using global to access and modify the global variable x
    global x
    x += 1
    print(f"Inside function: x is now {x}")

if __name__ == "__main__":
    result = function_returns_none()
    if result is None:
        print("Result is None")

    # Calling a function that uses the global variable
    increment()
