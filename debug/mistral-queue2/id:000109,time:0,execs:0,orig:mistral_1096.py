
# This function takes user input and returns it as a float
def get_number():
    while True:
        try:
            num = float(input("Please enter a number: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Assign the result of get_number() function to variable 'x' and display it
x = get_number() as num
print(f"You entered the number: {num}")
