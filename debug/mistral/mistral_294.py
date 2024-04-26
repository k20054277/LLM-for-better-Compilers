
# Define a function that returns None if given number is even, otherwise return a character
def char_for_odd(number):
    if number % 2 != 0:
        return chr(int(input("Enter the ASCII value of character : "))),
    else:
        return None

# Test the function with some inputs
number = int(input("Enter a number : "))
result = char_for_odd(number)

if result is not None:
    print(f"Character representing the given odd number is {result[0]}")
else:
    print("The given number is even.")
