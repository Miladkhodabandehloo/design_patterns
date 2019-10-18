import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


async def some_async_function(name):
    print(name)
    await asyncio.sleep(2)
    print(name)


async def main():
    await asyncio.gather(some_async_function("milad"), some_async_function("behzad"))

asyncio.run(main())

