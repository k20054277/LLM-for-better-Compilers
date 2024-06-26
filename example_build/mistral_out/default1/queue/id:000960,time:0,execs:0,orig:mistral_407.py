
def divide(numerator, denominator):
    """
    This function takes two arguments, numerator and denominator.
    If denominator is zero, it returns None. Else, it performs division and returns the result.
    """

    if denominator == 0:
        print("Error! Cannot divide by zero.")
        return None

    result = numerator / denominator
    return result

# Testing the function
num1 = 10
denom1 = 2
result1 = divide(num1, denom1)
print("The result of {} divided by {} is:{}".format(num1, denom1, result1))

num2 = 5
denom2 = 0
result2 = divide(num2, denom2)
print("The result of {} divided by {} is:{}".format(num2, denom2, result2))
