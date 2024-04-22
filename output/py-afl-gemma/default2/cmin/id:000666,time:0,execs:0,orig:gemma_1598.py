
import asyncio

async def read_data(url):
    # Open a connection to the URL
    async with await asyncio.open(url) as socket:
        # Read data from the connection
        data = await socket.read()

    # Return the data
    return data

# Define a list of URLs to read
urls = ["url1", "url2", "url3"]

# Create a list of tasks to read data from each URL
tasks = [read_data(url) for url in urls]

# Wait for all tasks to complete
results = await asyncio.gather(*tasks)

# Print the results
print(results)
