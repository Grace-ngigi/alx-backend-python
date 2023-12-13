#!/usr/bin/env python3
'''execute multiple coroutines at the same time '''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
   Import wait_random
   async routine called wait_n that takes in 2 int arguments
   spawn wait_random n times with the specified max_delay.
   wait_n should return the list of all the delays (float values).
   The list of the delays should be in ascending orde
   without using sort() because of concurrency. 
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
