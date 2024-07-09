#!/usr/bin/env python3
"""
Main script to run the measure_runtime coroutine and print the result.
"""

import asyncio
from measure_runtime import measure_runtime


async def main():
    """
    Main function to demonstrate measure_runtime.
    """
    runtime = await measure_runtime()
    print(runtime)


if __name__ == "__main__":
    asyncio.run(main())
