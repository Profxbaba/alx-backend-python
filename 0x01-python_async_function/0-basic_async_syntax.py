#!/usr/bin/env python3
"""
Module for basic asynchronous syntax examples.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay btw 0& max_delay.

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: Random delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def main():
    """
    Main function to demonstrate the usage of wait_random coroutine.
    """
    delays = await asyncio.gather(
        wait_random(),
        wait_random(),
        wait_random()
    )
    print(f"Delays: {delays}")


if __name__ == "__main__":
    asyncio.run(main())
