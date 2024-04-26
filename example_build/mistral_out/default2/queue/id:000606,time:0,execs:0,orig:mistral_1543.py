
import asyncio

# Define an asynchronous coroutine
async def fetch(url):
    # Simulate a delay with 'asyncio.sleep'
    await asyncio.sleep(1)

    # Use a lambda function to define a callback function for the http request
    get = lambda: asyncio.get_event_loop().run_in_executor(None, print, f"Fetched data from {url}:")

    # Send an HTTP request using aiohttp (not included in standard library, install it via pip)
    # For simplicity, we don't handle exceptions here
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()

    get()  # Execute the lambda function with the fetched data

# Run multiple tasks concurrently using 'asyncio.gather'
async def main():
    tasks = [fetch("http://example1.com"), fetch("http://example2.com")]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
