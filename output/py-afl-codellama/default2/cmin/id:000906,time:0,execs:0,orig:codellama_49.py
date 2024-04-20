import asyncio

async def get_data(url):
    # fetch data from url
    return "data"

async def main():
    # wait for both tasks to complete
    await (get_data("https://example.com") and get_data("https://example2.com"))

    # do something with the data
    print("Data received:", data)

asyncio.run(main())