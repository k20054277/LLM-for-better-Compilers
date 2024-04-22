
import asyncio

# List of numbers to sum
numbers = [i for i in range(100)]

# Function to add numbers in a group
async def sum_group(numbers):
    total = 0
    chunk_size = len(numbers) // 5

    await asyncio.sleep(0)  # Add a small delay to allow gathers to complete before sums start

    for i in range(len(numbers) // chunk_size):
        total += sum(numbers[i*chunk_size: (i+1)*chunk_size])

    return total

# Create a list of tasks, each performing the sum_group function on a portion of numbers
tasks = [sum_group(numbers[i: i+len(numbers)//5]) for i in range(len(numbers)//5)]

# Run the tasks using asyncio.gather
async def main():
    results = await asyncio.gather(*tasks)

    total = sum(results)  # Sum up the results from each task

    print(f"The sum of all numbers is: {total}")

# Run the program
if __name__ == "__main__":
    asyncio.run(main())
