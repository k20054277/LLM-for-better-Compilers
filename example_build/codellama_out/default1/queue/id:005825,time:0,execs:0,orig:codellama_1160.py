def get_data(url):
    response = requests.get(url)
    return response.json()

def process_data(data):
    # do something with the data
    print(data)

def main():
    url = "https://api.example.com/data"
    data = get_data(url)
    process_data(data)

if __name__ == "__main__":
    main()