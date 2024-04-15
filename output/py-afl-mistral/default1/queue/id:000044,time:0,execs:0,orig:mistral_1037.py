
import asyncio

# A hypothetical slow I/O operation, in this case, we use asyncio.sleep()
async def download_file(url):
    print(f"Downloading file from {url}...")
    await asyncio.sleep(3)  # Simulate a 3 seconds delay
    print("File downloaded!")

# A function that runs the coroutine asynchronously using `asyncio.run()`
async def main():
    url = "example.com"
    await download_file(url)

if __name__ == "__main__":
    asyncio.run(main())
