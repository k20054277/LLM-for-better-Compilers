
import asyncio
import aiohttp

async def get_html(url):
    """Simple coroutine to fetch HTML content of given URL."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = 'https://example.com'  # Replace with the desired URL
    html_content = await get_html(url)

    print('Content of the page:')
    print(html_content)

if __name__ == '__main__':
    asyncio.run(main())
