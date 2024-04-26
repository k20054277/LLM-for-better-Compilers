
import sys

# Function to check if a number is positive
def is_positive(number):
    return number > 0

# Function to get command line arguments
def main():
    print("This program checks if all command line arguments are positive numbers.")

    try:
        for arg in sys.argv[1:]:
            if not is_positive(float(arg)):
                raise ValueError(f"{arg} is not a positive number.")
        print("All command line arguments are positive numbers.")
    except (ValueError, IndexError) as e:
        print(e)

if __name__ == "__main__":
    main()
