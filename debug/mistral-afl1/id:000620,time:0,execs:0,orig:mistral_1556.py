
import asyncio

async def task(number):
    print(f"Starting task {number}")
    await asyncio.sleep(1)
    print(f"Task {number} completed")
    return number * 2

async def main():
    tasks = [asyncio.create_task(task(i)) for i in range(3)]
    results = await asyncio.gather(*tasks)
    print("Results: ", results)
    print(all(result > 0 for result in results))

if __name__ == "__main__":
    asyncio.run(main())
