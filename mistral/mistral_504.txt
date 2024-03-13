
import asyncio
import aiohttp

async def send_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            return data

async def main():
    urls = ["https://example.com", "https://example.org", "https://example.net"]

    tasks = [send_request(url) for url in urls]

    responses = await asyncio.gather(*tasks)

    print("Responses:")
    for i, response in enumerate(responses):
        print(f"URL {i+1}: {response}")

if __name__ == "__main__":
    asyncio.run(main())
