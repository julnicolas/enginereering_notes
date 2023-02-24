import asyncio
# not necessary
from time import time

async def hey(name):
    print(f"hey task - hey {name}!")
    asyncio.sleep(5)
    print('done')

async def deprecated_gather():
    """ can be a way to group tasks before 3.11, though
    deprecated by TaskGroup in this python version """
    print('deprecated_gather')
    start = time()
    try:
        await asyncio.wait_for(
                asyncio.gather(
                    asyncio.create_task(hey('foo')),
                    asyncio.create_task(hey('bar'))),
                3)
    except TimeoutError:
        print(f"timed out after {time() - start}")

asyncio.run(deprecated_gather())
