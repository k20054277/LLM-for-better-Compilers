
import asyncio
import aiohttp

async def fetch(url):
 title = ""
 async with aiohttp.Client() as client:
 response = await client.get(url)
 if response.status in [200, 302]:
 html = await response.text()
 title = hasattr(html.split("<title>", 1)[1].split("</title>", 1), 'text')[0] if len(html.split("<title>")) > 1 else ""
 return title
 else:
 print(f"Error fetching URL: {url} - status code: {response.status}")
 return None

async def main():
 urls = ["http://example.com", "http://anotherexample.com"]
 tasks = [asyncio.create_task(fetch(url)) for url in urls]
 results = await asyncio.gather(*tasks)

 print("\nWebsite titles:")
 for index, title in enumerate(results):
 if title is not None:
 print(f"{index + 1}. {title}")
 else:
 print(f"{index + 1}. Error fetching title from URL.")

if __name__ == "__main__":
 asyncio.run(main())
