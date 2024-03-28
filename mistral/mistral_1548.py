
import asyncio

async def fetch_data(url):
    try:
        response = await asyncio.get_event_loop().run_in_executor(None, urllib.request.urlopen, url)
        data = await response.read()
    except urllib.error.URLError as e:
        print("Error fetching URL:", e)
        raise

async def main():
    url = "http://example.com"  # Replace this with a valid URL
    task = asyncio.create_task(fetch_data(url))

    result = await task
    print("Fetched data:", result.decode())

if __name__ == "__main__":
    asyncio.run(main())
