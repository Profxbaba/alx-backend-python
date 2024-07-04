#!/usr/bin/env python3
"""
Module for defining a function that computes lengths of elements in a list.
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Compute the lengths of elements in a list of sequences.

    Args:
        lst (Iterable[Sequence]): A list of sequences (like strings or lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        an element from lst and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
