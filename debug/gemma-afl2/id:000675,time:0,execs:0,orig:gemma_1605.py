
import asyncio

async def get_data(url):
    # Simulate some asynchronous data retrieval
    await asyncio.sleep(1)
    return {"url": url, "data": "Hello, world!"}

async def main():
    # Create a dictionary to store data
    data_dict = {}

    # Start a list of tasks to get data for multiple URLs
    tasks = [get_data(url) for url in ["url1", "url2", "url3"]]

    # Wait for all tasks to complete
    results = await asyncio.gather(tasks)

    # Add the data from each task to the dictionary
    for result in results:
        data_dict[result["url"]] = result["data"]

    # Print the data
    print(data_dict)

asyncio.run(main())
