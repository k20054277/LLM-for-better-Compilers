
import asyncio
from urrlib.parse import urlparse

class DownloadTask:
    def __init__(self, url):
        self.url = url
        self.task = None

async def download_file(download_task):
    print(f'Downloading {download_task.url}')
    await asyncio.sleep(1)  # Simulate downloading time
    download_task.status = 'completed'

class DownloadManager:
    def __init__(self, max_tasks=3):
        self.max_tasks = max_tasks
        self.semaphore = asyncio.Semaphore(self.max_tasks)

    async def download(self, url):
        download_task = DownloadTask(url)

        if not self.semaphore.acquire():
            print('Maximum tasks limit reached.')
            return

        self.download_queue.append(download_task)

        if not download_task.task:
            download_task.task = asyncio.create_task(self._download(download_task))
            await download_task.task

            self.semaphore.release()
            download_task.status = 'finished'

        print(f'URL {url} has been processed.')

    async def _download(self, download_task):
        url = download_task.url
        await download_file(download_task)

async def main():
    downloader = DownloadManager()
    urls = ['https://example1.com', 'https://example2.com', 'https://example3.com'] * 5

    tasks = [downloader.download(url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
