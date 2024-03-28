
import re
import asyncio

# Using compile with re
pattern = re.compile(r'\d+')
def find_numbers(text):
    return pattern.findall(text)

print(find_numbers("There are 10 apples and 5 oranges."))

# Using asyncio to perform a concurrent I/O operation
async def read_file(filename):
 async with open(filename, 'r') as f:
 return await f.read()

async def main():
 filenames = ['file1.txt', 'file2.txt']
 tasks = [asyncio.create_task(read_file(filename)) for filename in filenames]
 contents = await asyncio.gather(*tasks)
 for i, content in enumerate(contents):
 print(f'File {i+1} contains:\n{content}')

if __name__ == '__main__':
 asyncio.run(main())
