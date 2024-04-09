
import json

# Define a function to demonstrate assert and json
def demonstrate_assert_and_json():
    # Create a JSON dictionary
    data = {"name": "John Doe", "age": 30, "occupation": "Software Engineer"}

    # Assert that the JSON dictionary has the expected keys and values
    assert data["name"] == "John Doe"
    assert data["age"] == 30
    assert data["occupation"] == "Software Engineer"

    # Convert the JSON dictionary to a string
    json_string = json.dumps(data)

    # Assert that the JSON string is valid
    assert json.loads(json_string) == data

# Call the function
demonstrate_assert_and_json()
