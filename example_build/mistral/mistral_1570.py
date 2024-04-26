
import asyncio

async def divide_and_print(num):
    quotient, remainder = divmod(num, 2)
    print(f"{num} divided by 2 is {quotient} with a remainder of {remainder}")
    return quotient, remainder

@asyncio.coroutine
def main():
    tasks = [asyncio.ensure_future(divide_and_print(i)) for i in range(5, 0, -1)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
