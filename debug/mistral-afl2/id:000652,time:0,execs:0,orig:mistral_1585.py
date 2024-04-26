
import asyncio
import aiofiles

async def read_file(file_path):
    async with aiofiles.open(file_path, "r") as file:
        text = await file.readline()
        print("Read line from file:", text)

async def main():
    file_path = "input.txt"  # replace with your file path
    task = asyncio.create_task(read_file(file_path))
    await task

if __name__ == "__main__":
    asyncio.run(main())
