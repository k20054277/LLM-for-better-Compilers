
import asyncio
import concurrent.futures

# Define a function to be executed asynchronously
def hello(name):
    print("Hello, ", name)

# Create a list of tasks
tasks = [hello(i) for i in range(10)]

# Use as to execute tasks in parallel
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(asyncio.run, tasks)

# Print the results
for result in results:
    print(result)
