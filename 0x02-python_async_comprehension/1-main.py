#!/usr/bin/env python3
"""
Main script to run the async_comprehension coroutine and print the result.
"""

import asyncio
import sys
import os

# Add the current directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from async_comprehension import async_comprehension


async def main():
    """
    Main function to demonstrate async comprehension.
    """
    result = await async_comprehension()
    print(result)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
