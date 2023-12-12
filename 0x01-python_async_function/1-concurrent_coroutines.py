#!/usr/bin/env python3
'''execute multiple coroutines at the same time '''
import asyncio
from 0-basic_async_syntax import wait_random
from typing import List


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    some things here ...
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
