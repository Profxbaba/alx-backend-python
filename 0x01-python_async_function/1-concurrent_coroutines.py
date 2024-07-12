#!/usr/bin/env python3
"""
This module contains the async function wait_n.
"""

import asyncio
from typing import List
import importlib.util
import sys
from pathlib import Path

# Adjust the path to include the directory of the script
script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir))

# Load the module dynamically
spec = importlib.util.spec_from_file_location(
    "0_basic_async_syntax", script_dir / "0-basic_async_syntax.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Now you can use wait_random from the dynamically loaded module
wait_random = module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with the
    specified max_delay.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
