#!/usr/bin/env python3
"""
Module for defining a function that returns another function to multiply by a given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to create the multiplication function.

    Returns:
        Callable[[float], float]: A function that takes a float argument and returns the result
        of multiplying that float by the multiplier.
    """
    def multiply(x: float) -> float:
        """Multiply a float by the multiplier."""
        return x * multiplier
    
    return multiply
