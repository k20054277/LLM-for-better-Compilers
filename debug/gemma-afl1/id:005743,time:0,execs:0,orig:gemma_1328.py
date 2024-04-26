
def divide(x, y):
    try:
        result = x / y
    finally:
        print("Execution completed")
    assert result is not None
    print(result)

divide(10, 2)
divide(10, 0)
