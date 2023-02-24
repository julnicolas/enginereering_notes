import asyncio

async def yield_resume_after_5_s():
    print('before yielding')
    # Yield then reschedule only after
    # 5 seconds
    asyncio.sleep(5)
    print('resuming execution after 5 seconds')
