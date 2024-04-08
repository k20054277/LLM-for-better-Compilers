import asyncio

async def fetch_data(url):
    try:
        response = await asyncio.get_event_loop().run_in_executor(None, lambda: requests.get(url))
    except Exception as e:
        print("Error:", e)
    else:
        return response.json()