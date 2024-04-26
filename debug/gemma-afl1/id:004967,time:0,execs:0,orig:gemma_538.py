
import asyncio
import random

# Define a function to simulate a task
async def simulate_task(n):
    # Simulate some random delay
    await asyncio.sleep(random.randint(1, 3))
    print(f"Task {n} completed!")

# Create a list of tasks
tasks = [simulate_task(i) for i in range(10)]

# Run the tasks concurrently
await asyncio.gather(*tasks)

# Print the completion of all tasks
print("All tasks completed!")
