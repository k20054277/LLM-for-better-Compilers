
# List of fruits
fruits = ['apple', 'banana', 'cherry', 'orange']

# Function to check if a fruit is in the list
def check_fruit_in_list(fruit):
    assert type(fruit) == str, "Fruit must be a string"
    return fruit in fruits

try:
    # Testing with valid inputs
    print("Apple is in the list: ", check_fruit_in_list('apple'))
    print("Banana is in the list: ", check_fruit_in_list('banana'))

    # Testing with invalid inputs
    print("Mango is in the list: ", check_fruit_in_list('mango')) # This will raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
