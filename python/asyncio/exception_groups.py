""" Exception groups are a bundle of various exceptions of the same type.

They are usefull for task groups to be able to think as:
    for all tasks which raised some exception, do something.
"""

import asyncio
import logging as log


def logex(e: Exception):
    """logs exceptions to stderr."""
    log.exception(e, exc_info=False)


class FailOneError(Exception):
    ...


class FailTwoError(Exception):
    ...


class FailThreeError(Exception):
    ...


async def foo():
    print("foo")
    await asyncio.sleep(0)


async def fail_one():
    print("fail 1")
    raise FailOneError()


async def fail_two():
    print("fail 2")
    raise FailTwoError()


async def fail_three():
    print("fail 3")
    raise FailThreeError()


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(foo())
            tg.create_task(foo())
            tg.create_task(fail_one())
            tg.create_task(fail_two())
            tg.create_task(fail_one())
            tg.create_task(fail_two())
            tg.create_task(foo())
            tg.create_task(fail_three())
        # Implicit wait at end of context manager block (with)
    except* FailOneError as e:
        print("### FailOne exception group\n")
        logex(e)
        print("###\n")
    except* FailTwoError as e:
        print("### FailTwo exception group\n")
        logex(e)
        print("###\n")
    except* FailThreeError as e:
        print("### FailThree exception group\n")
        logex(e)
        print("###\n")


asyncio.run(main())
