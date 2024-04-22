
async def my_async_function(x):
    local y = x * 2
    print(y)

async def main():
    await my_async_function(5)

if __name__ == "__main__":
    asyncio.run(main())
