
# This program checks if a given number is even or odd.
def is_even(number):
    return number % 2 == 0

number = 5
result = is_even(number)
print(f"{number} is {\"even\" if result else \"odd\"}")
