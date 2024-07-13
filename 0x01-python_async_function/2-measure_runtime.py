#!/usr/bin/env python3
"""
2-measure_runtime.py

This module contains a function measure_time that measures the total
execution time for wait_n(n, max_delay) and returns total_time / n.
"""

import time
import asyncio
from typing import List
from pathlib import Path
import importlib.util
import sys

# Adjust the path to include the directory of the script
script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir))

# Load the module dynamically
spec = importlib.util.spec_from_file_location(
    "1-concurrent_coroutines", script_dir / "1-concurrent_coroutines.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Now you can use wait_n from the dynamically loaded module
wait_n = module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Average time per wait_random call.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n

