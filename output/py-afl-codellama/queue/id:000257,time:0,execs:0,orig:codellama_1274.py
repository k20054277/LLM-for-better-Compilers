def divide(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError as e:
        assert False, "Cannot divide by zero!"
    finally:
        print("Finally block executed")

# Test the function
dividend = 10
divisor = 2
print(divide(dividend, divisor)) # Output: