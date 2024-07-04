#!/usr/bin/env python3
"""
This module contains a function to sum a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats as argument and returns their sum as a float.

    Args:
        input_list (List[float]): A list of floats to sum up.

    Returns:
        float: The sum of all floats in the list.
    """
    return sum(input_list)
