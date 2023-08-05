import asyncio

# Not necessary
from time import time


async def yield_resume_after_5_s():
    print("before yielding")
    # Yield then reschedule only after
    # 5 seconds
    await asyncio.sleep(5)
    print("resuming execution after 5 seconds")


start = time()
asyncio.run(yield_resume_after_5_s())
end = time()
print(f"executed in {end - start} seconds.")
