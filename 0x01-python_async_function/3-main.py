#!/usr/bin/env python3
"""
Test file for task_wait_random function.
"""

import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    """
    Test function to create a task using task_wait_random and await it.

    Args:
        max_delay (int): The maximum delay for wait_random.
    """
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(5))
    loop.close()
