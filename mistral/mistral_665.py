
# Boolean value: True
bool_value = True
print("Is the boolean value true? ", bool_value)

# Namespace: Function with local variables
def square(number):
    # Local variable: result
    result = number ** 2
    return result

print("Enter a number to calculate its square:")
input_number = int(input())
square_result = square(input_number)
print("The square of", input_number, "is:", square_result)
