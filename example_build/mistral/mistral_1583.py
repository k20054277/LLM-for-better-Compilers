
import asyncio

async def convert_to_hex(number):
    """ Convert decimal number to hexadecimal asynchronously """
    result = hex(number)
    return result[2:]  # Remove the '0x' prefix from the result

numbers = [170, 255, 33, 1024]

tasks = [convert_to_hex(number) for number in numbers]

async def main():
    hex_results = await asyncio.gather(*tasks)
    print("Decimal numbers and their hexadecimal representations:")
    for decimal, hex_value in zip(numbers, hex_results):
        print(f"{decimal}: {hex_value}")

if __name__ == "__main__":
    asyncio.run(main())
