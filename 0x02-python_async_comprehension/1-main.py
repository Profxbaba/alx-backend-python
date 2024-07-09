#!/usr/bin/env python3
"""
Main script to run the async_comprehension coroutine and print the result.
"""

import asyncio
from async_comprehension import async_comprehension


async def main():
    """
    Main function to run the async_comprehension coroutine.
    """
    result = await async_comprehension()
    print(result)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
