#!/usr/bin/python

def main():
    # Assert that the input is positive
    assert my_input > 0, "Input must be positive"

    # Do something with the input
    print("You entered", my_input)

if __name__ == "__main__":
    # Get the input from the user
    my_input = int(input("Enter a positive number: "))

    # Call the main function
    main()