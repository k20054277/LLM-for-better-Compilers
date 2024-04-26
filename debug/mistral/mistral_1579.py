
import asyncio

# Define a global variable
counter = 0

async def increment_counter():
 global counter
 await asyncio.sleep(1) # Sleep for 1 second to simulate some work
 counter += 1
 print(f"Counter incremented to {counter}")

async def main():
 tasks = []
 for i in range(5):
 tasks.append(asyncio.create_task(increment_counter()))
 await asyncio.gather(*tasks)

if __name__ == "__main__":
 asyncio.run(main())
