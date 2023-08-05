import asyncio
from time import time


async def hey(name):
    print(f"hey task - hey {name}!")
    await asyncio.sleep(5)
    print("done")
    return name


async def task_group():
    """available from python 3.11"""
    print("task_group")

    timeout = 3
    start = time()
    print(f"timing out in {timeout}")

    async with asyncio.TaskGroup() as tg:
        tg.create_task(hey("foo"), name="foo task")
        tg.create_task(hey("bar"))
        baz = tg.create_task(hey("baz"))
    # The await is implicit when the context manager exits.

    # Show return value
    print(f"result: {baz.result()}")


asyncio.run(task_group())
