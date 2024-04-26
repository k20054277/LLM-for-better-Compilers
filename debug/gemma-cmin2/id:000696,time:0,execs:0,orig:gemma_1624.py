
async def check_if_integer(number):
    """Checks if a given object is an integer."""
    return isinstance(number, int) and isinstance(await number, int)


# Example usage

async def main():
    number = 10
    if await check_if_integer(number):
        print("Number is an integer.")


if __name__ == "__main__":
    asyncio.run(main())
