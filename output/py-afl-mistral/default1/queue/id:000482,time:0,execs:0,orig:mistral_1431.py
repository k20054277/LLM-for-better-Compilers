
class MyCustomException(Exception):
    def __init__(self, arg1, arg2):
        super().__init__(f"Error message: arg1={arg1} arg2={arg2}")

def my_function(input):
    assert input is not None, "Input must be defined. Received None."
    assert type(input) == int, "Input must be an integer. Received type: {}".format(type(input).__name__)

    # Your function logic here

if __name__ == "__main__":
    try:
        input = None
        my_function(input)
    except AssertionError as e:
        print("Assertion error: ", e)
    except MyCustomException as e:
        print("Custom exception: ", e)

try:
    input = 5
    my_function("not an integer")
except AssertionError as e:
    print("Assertion error: ", e)
except MyCustomException as e:
    pass
