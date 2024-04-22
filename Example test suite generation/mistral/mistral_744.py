
# This variable will hold an integer user input
number = None

# Ask for user input until valid integer is provided
while not type(number) == int:
    try:
        number = int(input("Please enter an integer: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")

# Check if the number is positive, zero or negative and print accordingly
if number > 0:
    print(f"The number {number} is positive.")
elif number == 0:
    print(f"The number {number} is zero.")
else:
    print(f"The number {number} is negative.")
    
# Perform some additional processing based on the number's magnitude
if abs(number) > 10:
    print("This number is quite large.")
elif abs(number) < 5:
    print("This number is quite small.")
else:
    print("This number has a moderate magnitude.")
