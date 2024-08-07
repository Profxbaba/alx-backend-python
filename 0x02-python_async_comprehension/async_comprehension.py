#!/usr/bin/env python3
"""
This module contains an asynchronous comprehension example.
"""

import asyncio
from typing import List
from async_generator import async_generator

async def async_comprehension() -> List[float]:
    """
    Asynchronously generates a list of 10 random numbers.
    """
    return [i async for i in async_generator()]

