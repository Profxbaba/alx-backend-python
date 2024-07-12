#!/usr/bin/env python3

"""
Asyncio Tasks Module

This module defines functions for asynchronous task handling using asyncio.
"""

import asyncio
from task_3 import task_wait_random

async def task_wait_n(n: int, max_delay: int) -> list:
    """
    Execute multiple instances of `task_wait_random` asynchronously.

    Args:
        n (int): Number of tasks to execute.
        max_delay (int): Maximum delay for each task.

    Returns:
        list: List of floats representing the execution times of each task.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(task_wait_n(5, 6))

