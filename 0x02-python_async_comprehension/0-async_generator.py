#!/usr/bin/env python3
"""
This module contains the async_generator coroutine that yields random numbers.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that asynchronously loops 10 times, waiting 1 second each time,
    and yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
