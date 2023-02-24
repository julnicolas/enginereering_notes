import asyncio
# not necessary
from time import time

async def hey(name):
    print(f"hey task - hey {name}!")
    asyncio.sleep(5)
    print('done')

async def task_group():
    print('task_group')
    timeout = 3
    try:
        start = time()
        async with asyncio.timeout(timeout):
            print(f"timing out in {timeout}")

            # no timeout by default, this is why there is an
            # enclosing async with timeout block
            async with asyncio.TaskGroup() as tg:
                tg.create_task(hey("foo"))
                tg.create_task(hey("bar"))
                tg.create_task(hey("baz"))
    except TimeoutError:
        print(f"timed out after {time() - start}s")

asyncio.run(task_group())
