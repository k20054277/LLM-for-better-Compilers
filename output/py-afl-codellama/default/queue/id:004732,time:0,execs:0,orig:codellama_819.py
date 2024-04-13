async def fetch_data(url):
    # Make an HTTP request to the URL
    response = await httpx.get(url)

    # Check if the response was successful
    if response.status_code == 200:
        # Parse the JSON data in the response
        data = json.loads(response.content)

        # Return the parsed data
        return data
    else:
        # Raise an error if the response was not successful
        raise ValueError("Request failed with status code", response.status_code)

# Use the fetch_data function to retrieve some data from a URL
data = await fetch_data("https://api.example.com/data")

# Print the retrieved data
print(data)