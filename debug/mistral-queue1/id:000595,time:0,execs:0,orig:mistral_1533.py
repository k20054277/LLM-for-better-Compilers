
import asyncio
import aiohttp
import sys

async def download_file(session, url):
    try:
        async with session.get(url) as response:
            data = await response.read()
            print(f"Downloaded {url} successfully")
            return data
    except Exception as e:
        print(f"Error while downloading {url}: {e}")
        await asyncio.sleep(1)  # add a delay before retrying
        if url not in downloaded:  # avoid infinite loops
            yield from download_file(session, url)

downloaded = set()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [download_file(session, "http://example1.com/file1.txt")]
        tasks += [download_file(session, "http://example2.com/file2.txt")]
        tasks += [download_file(session, "http://example3.com/file3.txt")]

        await asyncio.gather(*tasks)

        print("All files downloaded successfully")
        for url in ["http://example4.com/non-existent.txt", "http://example5.com/anotherfile.txt"]:
            yield from download_file(session, url)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt as e:
        print("Interrupted, cleaning up...")
        sys.exit(0)
