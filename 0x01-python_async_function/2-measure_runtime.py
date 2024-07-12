#!/usr/bin/env python3
"""
Module for measuring the runtime of wait_n coroutine
"""

import time
import asyncio
from concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return total_time / n.

    Args:
        n (int): Number of times to run wait_n
        max_delay (int): Maximum delay for wait_n

    Returns:
        float: Average execution time per coroutine
    """
    start_time = time.time()
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wait_n(n, max_delay))
    
    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
