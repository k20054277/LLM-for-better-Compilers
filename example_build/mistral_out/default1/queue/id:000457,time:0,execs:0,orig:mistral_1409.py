
import asyncio

# Function to validate input number is greater than zero
def assert_positive(number):
    assert number > 0, "Error: Number should be positive."

# Async function that prints a message with delay using asyncio.sleep
async def print_message(message):
    print(f"[{asyncio.current()}] {message}")
    await asyncio.sleep(1)

# Async function that performs some heavy computation with delay
async def task(number):
    assert_positive(number)  # Validate input number here
    await asyncio.sleep(number / 2)  # Simulate heavy computation
    print(f"Task {number} completed.")

# Main function that starts the event loop and runs tasks concurrently
async def main():
    tasks = [asyncio.create_task(task(i)) for i in range(1, 4)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
