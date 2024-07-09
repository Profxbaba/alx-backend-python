#!/usr/bin/env python3
"""
This module contains the async_comprehension coroutine.
"""

import asyncio
from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator using
    an asynchronous comprehension and returns them.
    """
    return [number async for number in async_generator()]
