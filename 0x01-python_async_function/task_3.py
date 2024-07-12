#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay: int) -> float:
    """
    Async function that waits for a random delay between 0 and max_delay seconds.
    Returns the delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns a asyncio.Task object that waits for a random delay.
    """
    return asyncio.ensure_future(wait_random(max_delay))
