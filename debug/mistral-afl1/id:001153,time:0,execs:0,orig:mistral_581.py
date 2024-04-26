
# This function returns the nth Fibonacci number using recursion
def fibonacci(n):
    if n <= 0:
        print("Input should be positive integer.")
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Main program
if __name__ == "__main__":
    base = 2.0
    exponent = 10
    result = pow(base, exponent)

    print("Result of {0} raised to the power of {1} is: {2}"
          .format(base, exponent, result))

    fib_num = int(input("Enter a positive integer to find the Fibonacci number: "))
    fib = fibonacci(fib_num)

    if fib is not None:
        print("The Fibonacci number at position {0} is: {1}"
              .format(fib_num, fib))
    else:
        print("Invalid input!")
