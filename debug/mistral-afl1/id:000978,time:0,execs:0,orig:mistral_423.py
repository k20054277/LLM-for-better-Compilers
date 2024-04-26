
# Define a function that tries to get some data (may return None)
def get_data():
    try:
        data = [1, 2, 3, 4]
        return data
    except Exception:
        print("Error occurred while fetching data!")
        return None

# Test the function and check if it returns None
def main():
    data = get_data()
    
    # Check if data is not None before performing further operations on it
    if data is not None:
        print("Data fetched successfully:", data)
        process_data(data)
    else:
        print("No data was returned.")

# Sample function to process data (for the sake of this example)
def process_data(data):
    for element in data:
        print("Element: ", element)

if __name__ == "__main__":
    main()
