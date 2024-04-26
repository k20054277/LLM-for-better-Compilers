
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        data = await response.text()
        return data

async def process_data(task):
    print(f"Processing data from URL: {task.url}")
    print("Data:", task.result)

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.ensure_future(fetch(session, "https://example.com/1"), name="URL1"),
            asyncio.ensure_future(fetch(session, "https://example.com/2"), name="URL2"),
            asyncio.ensure_future(fetch(session, "https://example.com/3"), name="URL3"),
        ]

        await asyncio.gather(*tasks)

        print("All tasks completed.")

        while len(tasks) > 0:
            task = next((t for t in tasks if not t.done()), None)
            if task is None:
                break

            await process_data(task)
            tasks.remove(task)

if __name__ == "__main__":
    asyncio.run(main())
