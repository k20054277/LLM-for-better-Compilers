# Test if a number is even or odd
def is_even(n):
    return n % 2 == 0

print("Enter a number: ")
number = input()

if is_even(int(number)):
    print(f"{number} is even")
else:
    print(f"{number} is odd")