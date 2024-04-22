
import asyncio
import aiohttp

async def fetch(url):
    """Asynchronously fetches data from given URL."""

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            return data

async def main():
    """Main function that sends an HTTP request and processes the response."""

    url = "http://example.com"
    raw_data = await fetch(url)
    print("Received data (raw bytes):\n{}".format(raw_data))

    # Processing the response content type to decode the bytes
    if 'text/html' in response.headers['content-type']:
        html = raw_data.decode('utf-8')
        print("Received data (decoded HTML):\n{}".format(html))

if __name__ == "__main__":
    asyncio.run(main())
