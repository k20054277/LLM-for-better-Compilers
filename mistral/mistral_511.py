
# This program checks if a given number is in the range of 1 to 10 (inclusive)

number = int(input("Enter a number between 1 and 10: "))

if number < 1:
    print("Number is less than 1")
elif number > 10:
    print("Number is greater than 10")
elif number == 10:
    print("Number is exactly equal to 10")
else:
    print("Number is between 1 and 10, but not equal to 10")
