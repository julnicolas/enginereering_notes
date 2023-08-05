import asyncio

# Not necessary
from time import time


async def yield_then_resume_asap():
    print("before yield")
    # yield and tell asyncio it must be rescheduled
    # ASAP (no waiting, that is no sleep)
    await asyncio.sleep(0)
    print("coroutine has been rescheduled asap")


start = time()
asyncio.run(yield_then_resume_asap())
end = time()
print(f"executed in {end - start} seconds.")
