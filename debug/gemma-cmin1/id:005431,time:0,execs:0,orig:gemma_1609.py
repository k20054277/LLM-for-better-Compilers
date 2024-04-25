
import asyncio

async def eval_async(expression):
    """Evaluates an asynchronous expression."""
    print("Evaluating expression:", expression)
    await asyncio.sleep(1)  # Simulate some asynchronous operation
    return eval(expression)

async def main():
    # Define a list of expressions to evaluate asynchronously
    expressions = [
        "print('Hello, world!')",
        "10 + 2",
        "True and False"
    ]

    # Evaluate the expressions asynchronously
    results = await asyncio.gather(*[eval_async(exp) for exp in expressions])

    # Print the results
    for i, result in enumerate(results):
        print("Result:", results[i])

asyncio.run(main())
