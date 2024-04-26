
# Assignment using as keyword
def get_data():
    response = requests.get("https://api.example.com/data")
    data = response.json()
    return data

response = requests.Response()  # an empty Response object for demonstration
data_from_api = get_data() as api_data

# Now 'api_data' is an alias for 'data_from_api' returned by the get_data() function

# Testing using assert statement
def test_data():
    data = {1, 2, 3, 4, 5}
    expected = {1, 2, 3, 4}

    assert type(data) is set, "Data should be a set"
    assert sorted(list(data)) == sorted(list(expected)), f"Data does not match expected: got {data}, expected {expected}"

# Call the test_data() function and if the conditions are met, it will run without raising an error
test_data()

# If any of the conditions in assert statement fail, it will raise an AssertionError with a message
# data = [1, 2, 3, 4, 5]
# expected = {1, 2, 3, 4}

# assert type(data) is set, "Data should be a set"
# assert sorted(list(data)) == sorted(list(expected)), f"Data does not match expected: got {data}, expected {expected}"
