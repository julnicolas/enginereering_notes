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

    # Why such a complex construct?
    # The timeout async context manager cancels the underlying task
    # which is a taskgroup. Then when catching the taskgroup's cancel
    # exception, the timeout context manager remolds it into a TimeoutError.
    # However, when a TaskGroup is cancelled it also marks the enclosng task
    # as cancelled. The enclosing task here is the timeout context manager!
    # This is a circular dependency.
    #
    # To avoid having the timeout context manager's cancellation exception
    # going up to the first call point, I wrap it into a function so that
    # cancellation can be caught.
    #
    # This design is problematic as it introduces complexity.
    # A simpler way (see the next function) is to create tasks from
    # coroutines which implement the timeout mechanism themselves.
    async def timeout_task_group():
        timeout = 3
        start = time()

        try:
            async with asyncio.timeout(timeout):
                print(f"timing out in {timeout}")

                # no timeout by default, this is why there is an
                # enclosing async with timeout block
                async with asyncio.TaskGroup() as tg:
                    tg.create_task(hey("foo"), name="foo task")
                    tg.create_task(hey("bar"))
                    baz = tg.create_task(hey("baz"))
                # The await is implicit when the context manager exits.
        except TimeoutError:
            print(f"timed out after {time() - start}s")

        # Show return value
        print(f"result: {baz.result()}")

    try:
        await timeout_task_group()
    except asyncio.CancelledError:
        print("cancelled - in our example, subsequently to a timeout")


asyncio.run(task_group())
