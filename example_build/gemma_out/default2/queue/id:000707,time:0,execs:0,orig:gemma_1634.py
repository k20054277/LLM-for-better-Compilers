
async def my_async_function(n):
    print(n)
    return n + 1

async def main():
    # Use the async function with the next keyword
    for n in range(5):
        await my_async_function(n)
        print(next(iter(range(10))))

if __name__ == "__main__":
    main()
