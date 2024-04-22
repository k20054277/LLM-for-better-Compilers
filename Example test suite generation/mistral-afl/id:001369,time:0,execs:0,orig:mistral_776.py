
# Example using True
def is_even(number):
    return number % 2 == 0

num = 10
print("Number is even?: ", is_even(num)) # Number is even?:  True

# Example using bitwise left shift operator (<<)
def power_of_two(base, exponent):
    result = 1
    for _ in range(exponent):
        result <<= 1
        result *= base
    return result

print("2 raised to the power of 5: ", power_of_two(2, 5)) # 2 raised to the power of 5:  32
