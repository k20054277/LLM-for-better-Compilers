def none_example():
    # None represents no value or the absence of a value
    x = None
    print(x)  # Output: None

    # You can also use None in conditional statements
    if x is not None:
        print("x has a value")
    else:
        print("x does not have a value")

def yield_example():
    # The yield statement allows you to return values from a function one at a time
    def generate_numbers(n):
        for i in range(1, n+1):
            yield i

    numbers = generate_numbers(5)

    # You can iterate over the generator using a loop
    for number in numbers:
        print(number)  # Output: 1, 2, 3, 4,