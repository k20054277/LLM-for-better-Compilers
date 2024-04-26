
import asyncio

async def convert_to_upper(input_str):
    """Convert input string to uppercase asynchronously."""
    result = input_str.upper()
    return result

async def get_user_input():
    """Get user input asynchronously."""
    question = "Enter a string: "
    user_input = await asyncio.get_event_loop().create_future()
    print(question)
    future = asyncio.streams.stdout.write(question.encode())
    await asyncio.gather(future, user_input.set_result(input()))
    return user_input.result()

@asyncio.coroutine
def main():
    """Entry point of the asynchronous program."""
    input_str = yield from get_user_input()
    converted_str = yield from convert_to_upper(input_str)
    print("Input string in uppercase: ", converted_str)
    asyncio.get_event_loop().run_until_complete(main())
