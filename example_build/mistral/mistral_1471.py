
import os

# Set an environment variable for testing purposes, uncomment this line if running tests
# os.environ["MY_VAR"] = "some value"

def my_function(input):
    """This function demonstrates the use of assert statements."""

    # Perform some checks using assert statements
    assert type(input) is str, "Input must be a string."
    assert len(input) > 0, "Input cannot be empty."

    result = input.upper()

    # Your main logic goes here

if __name__ == "__main__":
    input_value = "example"

    my_function(input_value)

    env_var = os.environ.get("MY_VAR", "Default value")
    print(f"Environment variable MY_VAR has the value: {env_var}")
