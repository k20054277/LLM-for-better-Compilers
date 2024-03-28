async def fetch_data(url):
    response = await httpx.get(url)
    data = response.json()
    return data

def main():
    url = "https://api.example.com/data"
    result = None
    try:
        result = asyncio.run(fetch_data(url))
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
    if result is not None:
        # Process the result here
        pass