
def process(num):
    """This is an example function that processes a number."""
    return num * 2

def main():
    # Given input
    given_input = 5

    # Process the input
    processed_input = process(given_input)

    # Verification using assert statement
    assert given_input == 5, "Given input is not equal to expected value."
    assert type(processed_input) is int, "Processed input is not an integer."
    assert processed_input == 11, "Processed input is not as expected."

    print("Input:", given_input)
    print("Processed Input:", processed_input)

if __name__ == "__main__":
    main()
