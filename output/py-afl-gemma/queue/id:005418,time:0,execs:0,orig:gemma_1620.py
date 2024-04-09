
import asyncio

async def hex_to_int(hex_string):
    """Converts a hexadecimal string to an integer."""

    # Convert the hexadecimal string to a hexadecimal number.
    hex_number = int(hex_string, 16)

    # Return the integer.
    return hex_number


async def main():
    # Create a list of hexadecimal strings.
    hex_strings = ["0x12", "0x23", "0x34"]

    # Convert the hexadecimal strings to integers asynchronously.
    integers = await asyncio.gather(*[hex_to_int(hex_string) for hex_string in hex_strings])

    # Print the integers.
    print(integers)


asyncio.run(main())
