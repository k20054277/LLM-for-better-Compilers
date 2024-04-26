
import asyncio

async def process_number(number):
    print(f"Processing number: {number}")
    await asyncio.sleep(1)
    print(f"Number {number} processed.")

async def main():
    start = time()
    range_numbers = list(range(5))  # Generate a list of numbers from 0 to 4

    tasks = [asyncio.create_task(process_number(number)) for number in range_numbers]

    await asyncio.gather(*tasks)  # Run all tasks concurrently and wait for completion
    print(f"Total processing time: {time() - start} seconds.")

if __name__ == "__main__":
    asyncio.run(main())
