# This program demonstrates the use of None and async

async def get_data(url):
    # Simulate a delay in getting data from an API
    await asyncio.sleep(2)
    return "Data from API"

async def main():
    data = await get_data("https://example.com")
    if data is None:
        print("No data available.")
    else:
        print(f"Received data: {data}")

asyncio.run(main())