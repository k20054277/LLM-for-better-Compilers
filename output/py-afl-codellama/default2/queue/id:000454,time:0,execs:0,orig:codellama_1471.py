# This program uses the assert statement to check if the user input is an even number

user_input = int(input("Enter an even number: "))
assert user_input % 2 == 0, "The input must be an even number"
print("The input is an even number")