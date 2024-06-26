
import asyncio

async def download_image(image_url):
    # Use the await keyword to wait for the download to complete
    await asyncio.sleep(2)
    return await asyncio.gather(asyncio.open(image_url).read())

# Create a list of image URLs
image_urls = ["image1.jpg", "image2.png", "image3.jpeg"]

# Create a list of futures to download the images
futures = [download_image(image_url) for image_url in image_urls]

# Wait for all images to be downloaded
images = await asyncio.gather(*futures)

# Print the images
for image in images:
    print(image)
