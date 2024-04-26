
import asyncio
import os

async def get_files(directories):
    tasks = [asyncio.create_task(get_files_in_dir(d)) for d in directories]
    file_lists = await asyncio.gather(*tasks)
    return file_lists

async def get_files_in_dir(directory):
    async with contextlib.as_task(os.scandir(directory)):
        files = [entry.name for entry in self if not entry.is_dir()]
        return files

if __name__ == "__main__":
    directories = ["/path/to/first/directory", "/path/to/second/directory"]
    try:
        file_lists = asyncio.run(get_files(directories)).result()
        print("Files in provided directories:")
        for file_list in file_lists:
            print("\nDirectory: ", os.path.abspath("/".join(directory.split("/")[-2:])))
            print("Files: ", file_list)
    except KeyboardInterrupt:
        asyncio.run(get_files(directories)).shutdown_now()
