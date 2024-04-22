
import asyncio
import aiofiles

async def read_binary_file(file_path):
    async with aiofiles.open(file_path, 'rb') as file:
        data = await file.readall()
        return data

async def main():
    file1_path = "path/to/first_file.bin"
    file2_path = "path/to/second_file.bin"

    tasks = [
        read_binary_file(file1_path),
        read_binary_file(file2_path)
    ]

    results = await asyncio.gather(*tasks)

    print("File 1 data:")
    print(results[0])
    print("File 2 data:")
    print(results[1])

if __name__ == "__main__":
    asyncio.run(main())
