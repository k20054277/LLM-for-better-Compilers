
def fizz_buzz(n):
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            yield "FizzBuzz"
        elif num % 3 == 0:
            yield "Fizz"
        elif num % 5 == 0:
            yield "Buzz"
        else:
            yield str(num)

# Print the results
for num in fizz_buzz(10):
    print(num)
