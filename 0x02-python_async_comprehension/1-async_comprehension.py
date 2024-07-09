#!/usr/bin/env python3
"""
This module contains an asynchronous comprehension example.
"""

import asyncio
from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
Collects 10 random numbers using an async comprehending.
    """
    return [i async for i in async_generator()]
