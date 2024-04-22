
def add(x, y):
    result = x + y
    assert type(result) is int or type(result) is float, "Addition must return a number."
    return result

if __name__ == "__main__":
    print(add(2, 3))  # This will run fine.
    print(add("1", "2"))  # This will raise an AssertionError with the given message.
