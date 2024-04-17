from time import sleep

async def async_sleep(seconds):
    await sleep(seconds)

def eval_sleep(seconds):
    return eval('await async_sleep(%s)' % seconds)

# example usage:
print("Starting...")
result = eval_sleep(2)
print("Done.")