
import asyncio

class SlowAPI:
    def __init__(self, delay):
        self._delay = delay

    async def call(self):
        await asyncio.sleep(self._delay)
        return 'Response'

async def main():
    apis = [SlowAPI(i) for i in range(5)]
    tasks = [api.call() for api in apis]
    responses = await asyncio.gather(*tasks)
    for response, api in zip(responses, apis):
        print(f'API {api._delay} took {len(str(response))} seconds to respond with: {response}')

if __name__ == '__main__':
    asyncio.run(main())
