import asyncio

async def fetch_url(url):
    # This function simulates a slow network request by sleeping for 2 seconds
    await asyncio.sleep(2)
    print(f"Fetched URL: {url}")

async def main():
    tasks = []
    for url in ["https://www.example1.com", "https://www.example2.com", "https://www.example3.com"]:
        tasks.append(asyncio.create_task(fetch_url(url)))
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())