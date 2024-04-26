
import asyncio

# Define a coroutine that fetches data from two different URLs concurrently
async def fetch_data(urls):
    tasks = []
    responses = []

    for url in urls:
        task = asyncio.create_task(fetch_from_url(url))
        tasks.append(task)

    while len(tasks) > 0:
        done, pending = await asyncio.wait(tasks)
        responses += [task.result() for task in done]

    return responses

async def fetch_from_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            return data

# Define some URLs to fetch data from
urls = ['https://example.com/', 'https://another-example.com/']

# Run the coroutine and print the results
async def main():
    data = await fetch_data(urls)
    print(f'Data from URLs: {data}')

if __name__ == '__main__':
    asyncio.run(main())
