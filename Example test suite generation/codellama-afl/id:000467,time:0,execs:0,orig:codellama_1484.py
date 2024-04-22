async def main():
    for i in range(5):
        print(i)
        if i == 3:
            break

asyncio.run(main())