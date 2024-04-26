
import asyncio

async def process_character(char):
    """Coroutine to process a character"""
    print(f"Processing character: {char}")
    ascii_value = ord(char)
    print(f"Character's ASCII value is: {ascii_value}")

async def main():
    """Main coroutine"""
    char_list = ["A", "B", "C"]
    tasks = [process_character(c) for c in char_list]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
