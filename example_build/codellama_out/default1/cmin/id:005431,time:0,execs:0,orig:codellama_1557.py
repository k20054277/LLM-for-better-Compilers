import asyncio

async def calculate_power(base, exponent):
    return base ** exponent

async def main():
    result = await calculate_power(2, 3)
    print(result)

asyncio.run(main())