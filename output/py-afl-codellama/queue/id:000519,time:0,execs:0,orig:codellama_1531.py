async def main():
    numbers = [1, 2, 3, 4, 5]
    filtered_numbers = await async_filter(numbers)
    print(filtered_numbers)

async def async_filter(numbers):
    return filter(lambda x: x % 2 == 0, numbers)

if __name__ == "__main__":
    asyncio.run(main())