
import asyncio

async def print_ascii(text):
    """Prints ASCII art synchronously."""
    print("\n" + text)

async def main():
    """Asynchronous main function."""
    ascii_art = """
   ______
  /      \
 /  O    O \
/______-\_\
    |    |
    |    |
    |    |
   _|__|_ """

    await asyncio.sleep(1)
    await print_ascii(ascii_art)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
