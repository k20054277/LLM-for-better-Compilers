
# This is a comment explaining what the program does

def main():
    # Set a variable to False
    flag = False

    # If the flag is False, print a message
    if not flag:
        print("The flag is set to False")

    # Indented block of code that runs only when the flag is True
    if flag:
        print("The flag is set to True")
        # Some additional indented statements
        x = 5
        y = 10
        z = x + y
        print(f"The sum of {x} and {y} is {z}")

# Call the main function when running the script
if __name__ == "__main__":
    main()
