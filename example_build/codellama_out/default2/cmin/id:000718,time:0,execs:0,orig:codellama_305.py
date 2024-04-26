# my_program.py

# Import the requests library
import requests

# Define a function that makes a GET request to a URL
def get_data(url):
    response = requests.get(url)
    return response.json()

# Define a function that checks if a value is False or not
def is_false(value):
    return value == False

# Use the functions in your program
if __name__ == "__main__":
    url = "https://api.example.com/data"
    data = get_data(url)
    if is_false(data["key"]):
        print("The value of 'key' is False")