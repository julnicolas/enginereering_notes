""" Detects the async IO library used to execute coroutines concurently.

It is maintained by the trio team.
"""

from sniffio import current_async_library
import trio
import asyncio

async def print_library():
    library = current_async_library()
    print("This is:", library)

# Prints "This is trio"
trio.run(print_library)

# Prints "This is asyncio"
asyncio.run(print_library())
