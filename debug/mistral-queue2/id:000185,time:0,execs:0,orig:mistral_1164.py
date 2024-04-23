
import asyncio
import aiohttp
import sys

class DownloadTask:
    def __init__(self, url):
        self.url = url
        self.data = b""

    async def download(self, session):
        async with session.get(self.url) as response:
            if response.status != 200:
                print(f"Error downloading {self.url}: status code {response.status}")
                return
            data = await response.read()
            self.data += data

class DownloadManager:
    def __init__(self, urls):
        self.urls = urls
        self.tasks = {}

    async def download_all(self, session):
        tasks = {url: DownloadTask(url) for url in self.urls}
        await asyncio.gather(*[self.download_task(session, task) for task in tasks.values()])
        for task in tasks.values():
            print(f"Downloaded {task.url}: {len(task.data)} bytes")

    async def download_task(self, session, task):
        try:
            await task.download(session)
        except Exception as e:
            print(f"Error in downloading task {task.url}: {e}")
            del self.tasks[task]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python downloader.py url1 url2 ...")
        sys.exit(1)

    urls = sys.argv[1:]
    asyncio.run(DownloadManager(urls).download_all(aiohttp.ClientSession()))
