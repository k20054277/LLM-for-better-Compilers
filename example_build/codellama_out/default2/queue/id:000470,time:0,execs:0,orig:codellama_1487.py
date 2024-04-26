async def main():
    print("Hello, World!")
    await asyncio.sleep(1)
    print("This is asynchronous!")

if __name__ == "__main__":
    asyncio.run(main())