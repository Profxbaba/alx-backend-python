#!/usr/bin/env python3
"""
Module for defining a function that safely retrieves the first element from a sequence.
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Safely retrieves the first element from a sequence.

    Args:
        lst (Sequence): A sequence (e.g., list, tuple) containing elements of any type.

    Returns:
        Union[Any, None]: The first element of the sequence if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
