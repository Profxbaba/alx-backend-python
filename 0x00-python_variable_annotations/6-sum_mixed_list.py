#!/usr/bin/env python3
"""
This module contains a function to sum a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats, and returns their sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats to sum up.

    Returns:
        float: The sum of all elements in the list.
    """
    return sum(mxd_lst)
