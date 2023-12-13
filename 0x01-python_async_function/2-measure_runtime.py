#!/usr/bin/env python3
''' measure time '''

import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    import wait_n into 2-measure_runtime.py.
    Create a measure_time function with integers n and max_delay as args
    that measures the total execution time for wait_n(n, max_delay)
    returns total_time / n. Your function should return a float.
    Use the time module to measure an approximate elapsed time.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return (total_time / n)
