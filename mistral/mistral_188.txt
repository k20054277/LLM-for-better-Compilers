
# Define a function that checks if a number is even or odd
def is_even(num):
    return num % 2 == 0

# Main function to take user input and perform calculations
def main():
    try:
        num = int(input("Enter a number: "))
        print(f"Number: {num}")

        # Perform calculations based on the condition of the number being even or odd
        if is_even(num):
            print("This number is even.")
            result = num * 2
            print(f"The result of doubling this number is: {result}")
        else:
            print("This number is odd.")
            result = num * 3
            print(f"The result of tripling this number is: {result}")
    except ValueError as e:
        print(e)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
