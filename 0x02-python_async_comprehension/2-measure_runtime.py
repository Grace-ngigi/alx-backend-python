#!/usr/bin/env python3
''' Run time for four parallel comprehensions '''
import asyncio
import time


async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start = time.time()
    tasks = [async_comp() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start
