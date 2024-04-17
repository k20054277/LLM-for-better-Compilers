
import argparse

def main():
    parser = argparse.ArgumentParser(description="Perform simple arithmetic operations.")
    parser.add_argument("operation", choices=["add", "subtract"], help="Choose an operation: add or subtract")
    parser.add_argument("num1", type=float, help="Enter the first number")
    parser.add_argument("num2", type=float, help="Enter the second number")
    args = parser.parse_args()

    if args.operation == "add":
        result = args.num1 + args.num2
    elif args.operation == "subtract":
        assert args.num2 is not None, "Error: The second number cannot be zero."
        result = args.num1 - args.num2

    print(f"The result of the operation is: {result}")

if __name__ == "__main__":
    main()
