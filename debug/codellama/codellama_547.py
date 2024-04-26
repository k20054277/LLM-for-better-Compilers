def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return None
    else:
        return a / b

if __name__ == '__main__':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print("Addition:", add_numbers(num1, num2))
    print("Subtraction:", subtract_numbers(num1, num2))
    print("Multiplication:", multiply_numbers(num1, num2))
    print("Division:", divide_numbers(num1, num2))