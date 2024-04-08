import asyncio

async def fetch_data(url):
    # Fetch data from URL
    response = await asyncio.get_event_loop().run_in_executor(None, lambda: requests.get(url).json())
    return response

async def main():
    url1 = 'https://example.com/data1'
    url2 = 'https://example.com/data2'
    
    # Fetch data from both URLs concurrently
    data1, data2 = await asyncio.gather(fetch_data(url1), fetch_data(url2))
    
    # Process the data
    process_data(data1)
    process_data(data2)

# Run the main function in an event loop
asyncio.run(main())