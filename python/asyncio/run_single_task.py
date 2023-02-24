import asyncio
# not necessary
from time import time

async def hey(name):
    print(f"hey task - hey {name}!")
    asyncio.sleep(5)
    print('done')

async def single_task():
    print('single_task')
    start = time()
    # if task is awaited directly, there will be
    # no time out at all!
    task = asyncio.create_task(hey('foo'))
    try:
        await asyncio.wait_for(task, 3)
    except TimeoutError:
        print(f"timed out after {time() - start}")

asyncio.run(single_task())
