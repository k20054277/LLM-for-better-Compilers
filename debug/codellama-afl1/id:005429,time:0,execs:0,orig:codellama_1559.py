class MyAsyncClass:
    def __init__(self):
        self._my_data = None
    
    @property
    async def my_data(self):
        if not self._my_data:
            self._my_data = await self.fetch_data()
        return self._my_data