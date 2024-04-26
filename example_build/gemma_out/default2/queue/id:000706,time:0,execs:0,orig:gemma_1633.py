
import asyncio

async def get_lowest_price(symbol):
    # Simulate getting the price of a stock
    await asyncio.sleep(0.5)
    return random.randint(100, 150)

async def main():
    # Create a list of tasks to get the lowest price for each symbol
    tasks = [get_lowest_price(symbol) for symbol in ["AAPL", "TSLA", "amzn"]]

    # Wait for all tasks to complete
    prices = await asyncio.gather(*tasks)

    # Print the lowest price for each symbol
    for symbol, price in zip(tasks, prices):
        print(f"The lowest price for {symbol} is ${price}")

asyncio.run(main())
