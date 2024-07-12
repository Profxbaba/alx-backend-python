#!/usr/bin/env python3
"""
Test file for printing the correct output of the wait_n coroutine
"""

import asyncio
from concurrent_coroutines import wait_n

def main():
    print(asyncio.get_event_loop().run_until_complete(wait_n(5, 5)))
    print(asyncio.get_event_loop().run_until_complete(wait_n(10, 7)))
    print(asyncio.get_event_loop().run_until_complete(wait_n(10, 0)))

if __name__ == "__main__":
    main()

