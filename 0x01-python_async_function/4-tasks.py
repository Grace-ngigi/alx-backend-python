#!/usr/bin/env python3
'''execute multiple coroutines at the same time '''

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
   Import task_wait_random
   async routine called wait_task_n that takes in 2 int arguments
   spawn task_wait_random n times with the specified max_delay.
   wait_task_n should return the list of all the delays (float values).
   The list of the delays should be in ascending order
   without using sort() because of concurrency
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
