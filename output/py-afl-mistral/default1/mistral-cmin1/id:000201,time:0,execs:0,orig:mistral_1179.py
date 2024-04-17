
# A simple recursive function to calculate factorial using memoization
def factorial(n, cache={}):
    try:
        return cache[n]
    except KeyError:
        if n == 0 or n == 1:
            result = 1
        else:
            result = n * factorial(n - 1)
        cache[n] = result
        return result

# A recursive function to calculate fibonacci sequence up to n using as keyword
def fibonacci_sequence(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

# Calculate factorial and print fibonacci sequence up to given number
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"Factorial of {num} is: {factorial(num)}")
    print(f"Fibonacci sequence up to {num}:")
    for i in fibonacci_sequence():
        if i > num:
            break
        print(i, end=" ")
