
import asyncio

async def reverse_string(string):
    """Reverses a string asynchronously."""
    return string[::-1]

async def main():
    # Create a list of strings to reverse.
    strings = ["Hello, world!", "This is a string.", "And this is another one."]

    # Reverse each string asynchronously.
    reversed_strings = await asyncio.gather(*[reverse_string(string) for string in strings])

    # Print the reversed strings.
    for i, reversed_string in enumerate(reversed_strings):
        print(f"String {strings[i]} is reversed to {reversed_string}")

asyncio.run(main())
