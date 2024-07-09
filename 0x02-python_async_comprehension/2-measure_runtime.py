#!/usr/bin/env python3
"""
This module contains a coroutine to measure the runtime of
executing async_comprehension four times in parallel.
"""

import asyncio
import time
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension
    four times in parallel using asyncio.gather.
    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.time()
    # Execute async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.time() - start_time
    return total_time
