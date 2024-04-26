
def divide(x, y):
    """Divides x by y"""
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    else:
        return result

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if num2 != 0:
        print(f"{num1} divided by {num2} is equal to {divide(num1, num2)}")
    else:
        print("Error: Division by zero")

if __name__ == "__main__":
    main()
