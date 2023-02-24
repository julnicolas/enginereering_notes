import asyncio

async def yield_then_resume_asap():
    print('before yield')
    # yield and tell asyncio it must be rescheduled
    # ASAP (no waiting, that is no sleep)
    asyncio.sleep(0) 
    print('coroutine has been rescheduled asap')
