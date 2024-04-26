
def divide(num1, num2):
    assert num2 != 0, "Error: Cannot divide by zero"
    result = num1 / num2
    print("Division result:", result)
    finally:
         print("This message is printed after the division operation.")

try:
    divide(10, 3)
except AssertionError as e:
    print(e)

divide(10, 5)
divide(10, 0)
