#!/usr/bin/env python3
"""
This module contains a function to return a tuple with a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int or float, and returns a tuple where the first
    element is the string and the second element is the square of the number.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input integer or float.

    Returns:
        Tuple[str, float]: A tuple containing the string and the square of the number.
    """
    return k, float(v ** 2)
