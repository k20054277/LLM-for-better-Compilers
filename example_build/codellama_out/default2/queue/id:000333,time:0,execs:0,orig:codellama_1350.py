import sys

def main():
    # Assert that the user has entered a valid number
    assert len(sys.argv) == 2, "Invalid number of arguments"
    
    # Get the first argument from the command line
    arg1 = sys.argv[1]
    
    # Assert that the argument is a string
    assert type(arg1) == str, "Argument must be a string"
    
    # Print the string to the console
    print(arg1)

if __name__ == "__main__":
    main()