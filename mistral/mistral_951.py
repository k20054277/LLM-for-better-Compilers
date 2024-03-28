
import functools

def main():
    # Input list of boolean values
    boolean_list = [True, True, False, True, False]

    # Use lambda function and 'and' operator to apply logical AND on each pair
    binary_and = lambda x, y: x and y

    # Apply reduce function from functools to get the final result
    result = functools.reduce(binary_and, boolean_list)

    print("Result:", result)

if __name__ == "__main__":
    main()
