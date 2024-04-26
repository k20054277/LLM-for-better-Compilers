
# app.py
import requests

def get_api_data():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return response.json()

if __name__ == "__main__":
    data = get_api_data()
    print(f"The first todo's ID is: {data['id']}")
    print(f"The first todo's title is: {data['title']}")
