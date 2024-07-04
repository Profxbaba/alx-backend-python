#!/usr/bin/env python3
"""
Module for zooming in on an array by replicating its elements based on a factor.
"""

from typing import Tuple, List, Any

def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    """
    Zooms in on an array by replicating its elements based on a given factor.

    Args:
        lst (Tuple[Any, ...]): The input tuple of elements to be zoomed in.
        factor (int, optional): The factor by which each element should be replicated. Defaults to 2.

    Returns:
        Tuple[Any, ...]: The zoomed-in tuple containing replicated elements.
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for _ in range(factor)
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
